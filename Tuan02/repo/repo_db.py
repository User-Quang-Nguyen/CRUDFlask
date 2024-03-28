import psycopg2
import redis
import json
import logging

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
        redis_client = redis.Redis(host="localhost", port=6379)
        
        cache_key = f"get_profile_{name}"
        cached_data = redis_client.get(cache_key)
        if cached_data is not None:
            return cached_data.decode("utf-8")
        
        query = 'Select * from profile where name = %s'
        conn = self.get_connection()
        cur = conn.cursor()
        try:
            data = cur.execute(query, (name,))
            data = cur.fetchall()
            redis_client.setex(cache_key, 15*60, data)
            return data
        finally:
            cur.close()
            conn.close()
