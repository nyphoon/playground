import time
import datetime
from rq import get_current_job
from subprocess import Popen, PIPE, STDOUT


def run_command(cmd):
    p = Popen(cmd, stdout=PIPE, stderr=STDOUT, shell=True)
    stdout = p.stdout.read().decode()
    p.wait()
    print(f'complete command: {cmd} output: ')
    print(stdout)


def job_print(name=None):
    name = name or str(time.time())
    job_name = f'job_{name}'

    for i in range(5):
        print(job_name, i)
        time.sleep(1)


def _checkin_file(name):
    with open(name, 'a') as f:
        f.write(str(datetime.datetime.now()))
        f.write('\n')

def job_file(name=None):
    name = name or str(time.time())
    job_name = f'job_{name}'

    for i in range(5):
        _checkin_file(f'{job_name}.txt')
        time.sleep(1)

def job_exception(name):
    name = name or str(time.time())
    job_name = f'job_{name}'

    time.sleep(1)
    raise ValueError(job_name)

def job_progress(name):
    name = name or str(time.time())
    job_name = f'job_{name}'

    job = get_current_job()
    for i in range(5):
        job.meta['progress'] = 100 * i // 5
        job.save_meta()
        print(job_name, i)
        time.sleep(1)
        
    job.meta['progress'] = 100
    job.save_meta()
