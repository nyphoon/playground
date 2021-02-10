import time
from subprocess import Popen


if __name__ == '__main__':
    queue_names = ['q1', 'q2']
    procs = {}

    for q in queue_names:
        procs[q] = Popen(['python', 'worker.py', f'worker_{q}', q])

    while True:
        to_reopen = []
        for q, p in procs.items():
            if p.poll():
                to_reopen.append(q)
                print(
                    'worker (pid={}) of queue={} terminated in code={}'.format(
                        p.pid, q, p.returncode
                    ))

        for q in to_reopen:
            procs[q] = Popen(['python', 'worker.py', f'worker_{q}', q])
            print(f'worker of queue={q} reopened')

        time.sleep(5)
