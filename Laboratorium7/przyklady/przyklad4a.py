from redis import Redis

redis_connection = Redis(decode_responses=True)

redis_connection.zadd("posortowane_klucze",{"klucz1": 5})
redis_connection.zadd("posortowane_klucze",{"klucz2": 10})
redis_connection.zadd("posortowane_klucze",{"klucz3": 15})
redis_connection.zadd("posortowane_klucze",{"klucz4": 20})

print(redis_connection.zrange("posortowane_klucze",0, -1, withscores = True))