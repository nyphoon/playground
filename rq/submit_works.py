import time
from rq import Queue
from work import job_print, job_progress
from redis_connection import redis_conn


def submit(queue_name, arg):
    q = Queue(queue_name, connection=redis_conn, default_timeout=600)
    q.enqueue(job_print, arg)


def submit_and_monitor(works):
    # works is a dict in format {queue_name: args, ...}
    qs = {}

    for queue_name, args in works.items():
        for a in args:
            q = Queue(queue_name, connection=redis_conn)
            job = q.enqueue(job_progress, a)
            qs[f'{queue_name} - {a}'] = job
    
    while True:
        done = 0
        for a, job in qs.items():
            job.refresh()
            print(a, job.meta)

            # if not job.is_finished:
            if job.meta.get('progress') == 100:
                done += 1
        if done == len(qs):
            break
        time.sleep(1)
        print()
    print('all job done')

    

# one queue, one worker
# submit('q1', 'job_1')
# submit('q1', 'job_2')
# submit('q1', 'job_3')

# multi-queue, multi-woker
# submit('q1', 'job_a')
# submit('q2', 'job_b')
# submit('q1', 'job_c')
# submit('q2', 'job_d')

# multi-queue, multi-woker with progress
submit_and_monitor({'q1': ['a', 'b'],
                    'q2': ['c', 'd']})