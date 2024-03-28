from flask import request
from ulti.input_validation import InputValidationException
class RequestDTO: 
    def __init__(self, request):
        self.request = request
    
    def check_input_name(self):
        if self.request.is_json == False:
            raise InputValidationException("Missing JSON data in request")
        if self.request.json.get('name') == "" or len(self.request.json) == 0:
            raise InputValidationException("Hollow input")