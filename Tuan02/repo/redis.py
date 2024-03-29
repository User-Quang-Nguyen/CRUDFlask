import redis
import ast
import json
from flask import jsonify


class RedisCache:
    def __init__(self) -> None:
        self.host = "localhost"
        self.port = "6379"

    def connect_redis(self):
        try:
            redis_client = redis.Redis(host=self.port, port=self.port, decode_responses=True)
            print(redis_client.ping())
            return redis_client
        except Exception as e:
            return None
        
    def check_cache(self, key):
        try:
            redis_client = self.connect_redis()
            cached_data = redis_client.get(key)
            
            if cached_data is not None:
                my_data = ast.literal_eval(cached_data)
                return my_data
        except Exception as e:
            print("error: ", e)
            pass
            
    def set_cache(self, key, data):
        redis_client = self.connect_redis()
        json_string = json.dumps(data)
        try:
            redis_client.setex(key, 15*60, json_string)
        except Exception as e:
            print("error: ", e)
            pass