from flask import Flask
from ulti.input_validation import InputValidationException

class ResponseDTO:
    def __init__(self) -> None:
        pass
    
    def response_infor(self, list_response):
        # if len(list_response) == 0:
        #     raise InputValidationException("User does not exist")
        response_json = []
        for item in list_response:
            response_json.append({
                "id": item[0],
                "name": item[1],
                "address": item[2],
                "job": item[3],
                "phone": item[4]
            })
            
        return response_json