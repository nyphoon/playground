from rq import Queue
from redis_connection import redis_conn
from work import run_command


def submit_script(queue_name, command):
    q = Queue(queue_name, connection=redis_conn, default_timeout=600)
    q.enqueue(run_command, command)


submit_script('q1', ['python job_print.py a'])
submit_script('q2', ['python job_file.py b'])
submit_script('q1', ['ls', '-a'])
submit_script('q2', ['python job_exception.py'])
