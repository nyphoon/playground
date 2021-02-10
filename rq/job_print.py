import sys
from work import job_print


if __name__ == '__main__':
    name = None
    if len(sys.argv) >= 2:
        name = sys.argv[1]
    
    job_print(name)
