from redis import Redis

redis_connection = Redis(decode_responses=True)

key ="klucz2b"
value ="wartosc2b"

redis_connection.set(key, value)
print(redis_connection.get(key))

redis_connection.append(key,"-append")
print(redis_connection.get(key))

redis_connection.delete(key)
print(redis_connection.get(key))