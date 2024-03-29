import flask
from flask import jsonify, request
from minio import Minio
from minio.error import S3Error
app = flask.Blueprint("file", __name__)

# Chưa tách các thành phần
@app.route('/file', methods = ["POST"])
def upload():
    try:
        client = Minio("127.0.0.1:9000", access_key = 'minioadmin', secret_key = 'minioadmin', secure = False)
        
        my_data = request.json
        source_file = my_data.get('src')
        bucket_name = "python-test-bucket"
        destination_file = 'op.jpg'
        
        found = client.bucket_exists(bucket_name)
        print("success")
        if not found:
            client.make_bucket(bucket_name)
            print("Created bucket", bucket_name)
        else:
            print("Bucket", bucket_name, " already exist")
        
        client.fput_object(
            bucket_name, destination_file, source_file,
        )
        print(
            source_file, "Successfully uploaded as object",
            destination_file, "to bucket", bucket_name,
        )
        return jsonify({"URL Image": "http://127.0.0.1:9000/" + bucket_name + '/' + destination_file}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": e}), 400