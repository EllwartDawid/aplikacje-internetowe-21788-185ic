from redis import Redis

redis_connection = Redis(decode_responses=True)

list_key ="lista-przykladowa"

while True:
    print(redis_connection.brpop(list_key))