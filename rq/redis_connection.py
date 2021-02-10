from redis import Redis


REDIS_HOST = '10.188.243.109'
REDIS_PORT = '6379'
REDIS_PASSWORD = '123qwertyUI'
redis_conn = Redis(
    host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)
