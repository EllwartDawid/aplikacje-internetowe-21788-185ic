from redis import Redis


redis_connection = Redis(decode_responses=True)

key ="klucz2c"
value =100

redis_connection.set(key, value)

print(redis_connection.get(key))

print(redis_connection.incr(key,20))

print(redis_connection.decr(key,80))