import sys
from rq import Worker
from redis_connection import redis_conn


def clean_worker(redis_conn, name):
    for k in redis_conn.keys(f'*:{name}'):
        redis_conn.delete(k)


def work(redis_conn, name, queue_id):
    worker = Worker([queue_id], connection=redis_conn, name=name)
    try:
        worker.work()
    except Exception as e:
        print('worker error', e)


if __name__ == '__main__':
    worker_name = sys.argv[1]
    queue_name = sys.argv[2]

    clean_worker(redis_conn, worker_name)
    work(redis_conn, worker_name, queue_name)
    sys.exit(1)  # code runs to here only if work happens exception
