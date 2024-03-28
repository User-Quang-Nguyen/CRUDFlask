from flask import Flask, request, jsonify
from handler import bootstrap
from api_dto.request import RequestDTO
from api_dto.response import ResponseDTO
import flask

app = flask.Blueprint("profile", __name__)
requestdto = RequestDTO(request=request)
responsedto = ResponseDTO()
@app.route('/data/profile', methods=['POST'])
def read_infor():
    try: 
        requestdto.check_input_name()
        my_data = request.json
        name = my_data.get('name')
        res = bootstrap.get_data_profile(name = name)
        result = responsedto.response_infor(res)
        return result
    except Exception as e:
        return jsonify({"message": str(e)}), 400