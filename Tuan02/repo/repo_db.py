from flask import Flask, request, jsonify
import psycopg2
import logging


class PostgreDatabase:
    def __init__(self):
        self.postgre_host = ''
        self.postgre_port = ''
        self.db_user = ''
        self.db_pass = ''
        self.db = ''

    def get_connection(self):
        try:
            conn = psycopg2.connect(database='flask_db', user='postgres',
                                password='12345678', host='localhost', port='5432')
            return conn
        except Exception as e:
            logging.getLogger().info(f"[ERROR] connection refuse: {str(e)}")

    def create_table(self):
        try:
            '''
            '''
        except Exception as e:
            logging.getLogger().info(f"[ERROR] create table: {str(e)}")

    def get_profile(self, name):
        conn = self.get_connection()
        cur = conn.cursor()
        try:
            cur = conn.cursor()
            data = cur.execute('Select * from profile where name = %s',(name,))
            data = cur.fetchall()
            return data
        except Exception as e:
            logging.getLogger().info(f'[ERROR] get info data: {str(e)}')
        finally:
            cur.close()
            conn.close()



#
#
#
# def connect_db():
#     try:
#         conn = psycopg2.connect(database='flask_db', user='postgres',
#                                 password='12345678', host='localhost', port='5432')
#
#         print("Connected!")
#         return conn
#     except Exception as e:
#         print("Faild!", e)
#         return None
#
#
# def create_table():
#     conn = connect_db()
#     try:
#         cur = conn.cursor()
#         cur.execute(
#             '''Create table if not exists profile
#                 (id serial primary key,
#                 name varchar(30),
#                 address varchar(200),
#                 job varchar(20),
#                 phone_number varchar(15));
#             '''
#         )
#         conn.commit()
#         cur.close()
#         conn.close()
#     except Exception as e:
#         print("Faild", e)
#
#
