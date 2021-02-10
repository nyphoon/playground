import time
from multiprocessing import Process
from rq import Worker
from redis_connection import redis_conn


def clean_worker(redis_conn, name):
    for k in redis_conn.keys(f'*:{name}'):
        redis_conn.delete(k)


def work(redis_conn, name, queue_name):
    worker = Worker([queue_name], connection=redis_conn, name=name)
    try:
        worker.work()
    except Exception as e:
        print('worker error', e)
    # TODO: how to set Process.exitcode


if __name__ == '__main__':
    queue_names = ['q1', 'q2']
    procs = {}

    for q in queue_names:
        clean_worker(redis_conn, q)
        procs[q] = Process(target=work, args=(redis_conn, f'worker_{q}', q))
        procs[q].start()

    while True:
        to_reopen = []
        for q, p in procs.items():
            if not p.is_alive():
                to_reopen.append(q)
                print(
                    'worker (pid={}) of queue={} terminated in code={}'.format(
                        p.pid, q, p.exitcode
                    ))

        for q in to_reopen:
            procs[q] = Process(target=work, args=(redis_conn, f'worker_{q}', q))
            procs[q].start()
            print(f'worker of queue={q} restarted')

        time.sleep(5)
