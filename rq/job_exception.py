import sys
from work import job_exception


if __name__ == '__main__':
    name = None
    if len(sys.argv) >= 2:
        name = sys.argv[1]

    job_exception(name)
