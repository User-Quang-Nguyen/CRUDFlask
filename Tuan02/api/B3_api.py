from flask import Flask, request, jsonify
import flask

app = flask.Blueprint("api_app", __name__)


# @app.route('/data/profile', methods=['POST'])
# def read_infor():
#     try:
#         name = request.form['name']
#         cur = conn.cursor()                          # Not get connection db in handler body request !!!

#         data = cur.execute('Select * from profile where name = %s',(name,))
#         data = cur.fetchall()
#         cur.close()
#         conn.close()
#         return data
#     except Exception as e:
#         return None
    
# if __name__ == '__main__':
#     create_table()
#     app.run(debug = True)