from flask import Flask, jsonify

app = Flask(__name__)
    
@app.route('/', methods=['GET'])
def service():
    response = jsonify()
    response.status_code = 200
    return response

if __name__ == '__main__':
    app.run(debug=True, port=8000)