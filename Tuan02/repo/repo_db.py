import psycopg2
import redis
import json
import ast
import logging
from ulti.cache_error import CacheError

class PostgreDatabase:
    def __init__(self):
        self.postgre_host = 'localhost'
        self.postgre_port = '5432'
        self.db_user = 'postgres'
        self.db_pass = '12345678'
        self.db = 'flask_db'

    def get_connection(self):
        try:
            conn = psycopg2.connect(database=self.db, user=self.db_user,
                                password=self.db_pass, host=self.postgre_host, port=self.postgre_port)
            return conn
        except Exception as e:
            logging.getLogger().info(f"[ERROR] connection refuse: {str(e)}")

    def create_table(self, command):
        try:
            conn = self.get_connection()
            cur = conn.cursor()
            cur.execute(command)
            conn.commit()
        finally:
            cur.close()
            conn.close()

    def get_profile(self, name):
        cache_key = f"get_profile_{name}"
        try:
            redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)
            cached_data = redis_client.get(cache_key)
            
            if cached_data is not None:
                my_data = ast.literal_eval(cached_data)
                print("Cache redis")
                return my_data
            
        except Exception as e:
            raise CacheError("Redis server is not running")
        
        query = 'Select * from profile where name = %s'
        conn = self.get_connection()
        cur = conn.cursor()
        try:
            data = cur.execute(query, (name,))
            data = cur.fetchall()
            
            json_string = json.dumps(data)
            redis_client.setex(cache_key, 15*60, json_string)
            cached_data = redis_client.get(cache_key)
            
            print("Postgres")
            return data
        finally:
            cur.close()
            conn.close()
