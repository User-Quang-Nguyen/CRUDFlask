import psycopg2
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
        conn = self.get_connection()
        cur = conn.cursor()
        try:
            cur = conn.cursor()
            data = cur.execute('Select * from profile where name = %s',(name,))
            data = cur.fetchall()
            return data
        finally:
            cur.close()
            conn.close()
