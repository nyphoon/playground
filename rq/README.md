# How to run demo

### one queue, one woker
* start worker
```
python worker.py worker_q1 q1
```
* submit work
```
python submit_works.py
```

### multi-queue, multi-woker
* start worker
    * * edit `queue_names` in `submit_works.py` to have more queue and workers
```
python works.py
```
* submit work
    * edit to call more submit in `submit_works.py`
```
python submit_works.py
```

### multi-queue, multi-woker to run any command in subprocess
* start worker
```
python works.py
```
* submit work
```
python submit_commands.py
```
