from redis import Redis


redis_connection = Redis(decode_responses=True)

list_key ="lista-przykladowa"

redis_connection.rpush(list_key,1,3,5,7,13)

print(redis_connection.lrange(list_key,3,5))