from flask import request, jsonify
from services import calculator
import os

def operation_endpoints(app,route_api):

    @app.route(route_api+'/operations', methods=["POST"])
    def getOperations():
        res = calculator.getOperations_()
        return res


    @app.route(route_api+'/operations/<user_id>', methods=["POST"])
    def getRecords(user_id):
        try:
            id = int(user_id)
        except ValueError:
            return {'msg': 'Bad parameters int needed'}
        res = calculator.getRecords_(id)
        return res
    

    @app.route(route_api+'/sum', methods=["POST"])
    def sum():
        try:
            v1 = float(request.json.get('v1'))
            v2 = float(request.json.get('v2'))
        except ValueError:
            response =  jsonify({'message': 'ValueError is not a int or float'})
            return response, 400

        if( type(v1) not in [int,float] or type(v2) not in [int,float]):
            response =  jsonify({'message': 'Error is not a int or float'})
            return response, 400
        response = round(calculator.sum_(v1,v2),2)
        return {'result': response}

    
    @app.route(route_api+'/sub', methods=["POST"])
    def sub():
        try:
            v1 = float(request.json.get('v1'))
            v2 = float(request.json.get('v2'))
        except ValueError:
            response =  jsonify({'message': 'ValueError is not a int or float'})
            return response, 400

        response = calculator.sub_(v1,v2)
        return {'result': response}


    @app.route(route_api+'/mult', methods=["POST"])
    def mult():
        try:
            v1 = float(request.json.get('v1'))
            v2 = float(request.json.get('v2'))
        except ValueError:
            response =  jsonify({'message': 'ValueError is not a int or float'})
            return response, 400

        response = calculator.mult_(v1,v2)
        return {'result': response}

    @app.route(route_api+'/div', methods=["POST"])
    def div():
        try:
            v1 = float(request.json.get('v1'))
            v2 = float(request.json.get('v2'))
        except ValueError:
            response =  jsonify({'message': 'ValueError is not a int or float'})
            return response, 400

        response = calculator.div_(v1,v2)
        return {'result': response}

    @app.route(route_api+'/square_root', methods=["POST"])
    def square_root():
        try:
            v1 = float(request.json.get('v1'))
        except ValueError:
            response =  jsonify({'message': 'ValueError is not a int or float'})
            return response, 400

        response = calculator.sqrt_(v1)
        return {'result': response}

    @app.route(route_api+'/rand_string', methods=["POST"])
    def rand_string():
        response = calculator.rand_str_()
        return { 'result': response }