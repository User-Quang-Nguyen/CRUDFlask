from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

def connect_db():
    try:
        conn = psycopg2.connect(database = 'flask_db', user = 'postgres', 
                                password = '12345678', host = 'localhost', port = '5432')

        print("Connected!")
        return conn
    except Exception as e:
        print("Faild!", e)
        return None

def create_table():
    conn = connect_db()
    try:
        cur = conn.cursor()
        cur.execute(
            '''Create table if not exists profile
                (id serial primary key,
                name varchar(30),
                address varchar(200),
                job varchar(20),
                phone_number varchar(15));
            '''
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print("Faild", e)

@app.route('/data/profile', methods=['POST'])
def read_infor():
    try:
        conn = connect_db()
        name = request.form['name']
        cur = conn.cursor()
        data = cur.execute('Select * from profile where name = %s',(name,))
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
    except Exception as e:
        return None
    
if __name__ == '__main__':
    create_table()
    app.run(debug = True)