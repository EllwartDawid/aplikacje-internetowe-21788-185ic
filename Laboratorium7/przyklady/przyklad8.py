from redis import Redis

redis_connection = Redis(decode_responses=True, db=0)


script ="""
return "testowanie"
"""

print(redis_connection.eval(script,0))