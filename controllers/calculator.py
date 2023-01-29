from flask import request, jsonify
from services import calculator
import os
import requests



def operation_endpoints(app,route_api):

    @app.route(route_api+'/operations', methods=["POST"])
    def getOperations():
        res = calculator.getOperations_
        return res

    
    @app.route(route_api+'/operations/cost/<type_>', methods=["POST"])
    def getOperations_by_type(type_):
        
        res = calculator.getOperations_by_type_(type_)
        

        try: 
            response = {'id': res["id"], 'type': res["type"], 'cost': res.cost }
        except KeyError:
            response={ 'message': 'Operation not found'}
        except ValueError:
            response={ 'message': 'Operation not found'}
        except TypeError:
            response={ 'message': 'Operation not found'}
        return response


    @app.route(route_api+'/records/<user_id>', methods=["POST"])
    def getRecords(user_id):
        try:
            id = int(user_id)
        except ValueError:
            return {'msg': 'Bad parameters int needed'}
        res = calculator.getRecords_(id)
        return res
    
    @app.route(route_api+'/records/<id>', methods=["DELETE"])
    def deleteRecords(id):
        try:
            id = int(id)
        except ValueError:
            return {'msg': 'Bad parameters int needed'}
        res = calculator.deleteRecord_(id)
        return {'message': f'Deleted id: {id} '}
    

    @app.route(route_api+'/sum', methods=["POST"])
    def sum():
        try:
            v1 = float(request.json.get('v1'))
            v2 = float(request.json.get('v2'))
            user_id = int(request.json.get('user_id'))
            operation = 'addition'
            user_balance = int(request.json.get('user_balance'))
            
        except ValueError:
            response =  jsonify({'message': 'ValueError is not a int or float'})
            return response, 400
        except TypeError:
            response =  jsonify({'message': 'TypeError is not a int or float'})
            return response, 400

        if( type(v1) not in [int,float] or type(v2) not in [int,float]):
            response =  jsonify({'message': 'Error is not a int or float'})
            return response, 400
        
        response = calculator.sum_(v1,v2, user_id, operation, user_balance)        
        return response

    
    @app.route(route_api+'/sub', methods=["POST"])
    def sub():
        try:
            v1 = float(request.json.get('v1'))
            v2 = float(request.json.get('v2'))
            user_id = int(request.json.get('user_id'))
            operation = 'substraction'
            user_balance = int(request.json.get('user_balance'))
            
        except ValueError:
            response =  jsonify({'message': 'ValueError is not a int or float'})
            return response, 400
        except TypeError:
            response =  jsonify({'message': 'TypeError is not a int or float'})
            return response, 400

        if( type(v1) not in [int,float] or type(v2) not in [int,float]):
            response =  jsonify({'message': 'Error is not a int or float'})
            return response, 400
        
        response = calculator.sub_(v1,v2, user_id, operation, user_balance)        
        return response


    @app.route(route_api+'/mult', methods=["POST"])
    def mult():
        try:
            v1 = float(request.json.get('v1'))
            v2 = float(request.json.get('v2'))
            user_id = int(request.json.get('user_id'))
            operation = 'multiplication'
            user_balance = int(request.json.get('user_balance'))

        except ValueError:
            response =  jsonify({'message': 'ValueError is not a int or float'})
            return response, 400
        except TypeError:
            response =  jsonify({'message': 'TypeError is not a int or float'})
            return response, 400

        response = calculator.mult_(v1,v2, user_id, operation, user_balance)
        return response


    @app.route(route_api+'/div', methods=["POST"])
    def div():
        try:
            v1 = float(request.json.get('v1'))
            v2 = float(request.json.get('v2'))
            user_id = int(request.json.get('user_id'))
            operation = 'division'
            user_balance = int(request.json.get('user_balance'))
        except ValueError:
            response =  jsonify({'message': 'ValueError is not a int or float'})
            return response, 400
        except TypeError:
            response =  jsonify({'message': 'TypeError is not a int or float'})
            return response, 400

        response = calculator.div_(v1,v2, user_id, operation, user_balance)
        return response


    @app.route(route_api+'/square_root', methods=["POST"])
    def square_root():
        try:
            v1 = float(request.json.get('v1'))
            user_id = int(request.json.get('user_id'))
            operation = 'square_root'
            user_balance = int(request.json.get('user_balance'))
        except ValueError:
            response =  jsonify({'message': 'ValueError is not a int or float'})
            return response, 400
        except TypeError:
            response =  jsonify({'message': 'TypeError is not a int or float'})
            return response, 400

        if (v1 < 0):
            response =  jsonify({'message': 'Need a positive value'})
            return response, 400

        response = calculator.sqrt_(v1, user_id, operation, user_balance)
        return response


    @app.route(route_api+'/random_string', methods=["POST"])
    def rand_string():
        url_random_org_string='https://api.random.org/json-rpc/2/invoke'
        try:
            user_id = int(request.json.get('user_id'))
            operation = 'random_string'
            user_balance = int(request.json.get('user_balance'))
        except ValueError:
            response =  jsonify({'message': 'ValueError is not a int or float'})
            return response, 400
        except TypeError:
            response =  jsonify({'message': 'TypeError is not a int or float'})
            return response, 400

        
        data = requests.post(url_random_org_string, json = {
            "jsonrpc": "2.0",
            "method": "generateStrings",
            "params": {
                "apiKey": "577e944c-bed5-42aa-949e-ce6f6fa4dfb4",
                "n": 1,
                "length": 8,
                "characters": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&*",
            "replacement": False
            },
            "id": 3076
        })
        if data.status_code == 200:
            data=data.json()
            result = data['result']['random']['data'][0]
        else:
            response = {'message': f'Error trying to get random string StatusCode: {data.status_code}'}

        response = calculator.rand_str_(user_id, operation, user_balance,result)
        return response