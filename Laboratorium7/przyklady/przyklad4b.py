from redis import Redis

redis_connection = Redis(decode_responses=True)

hash_key ='hash-testowy'

redis_connection.hset(hash_key,'klucz','wartosc')