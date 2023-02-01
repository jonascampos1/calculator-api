from flask import request, jsonify
from services import calculator
from services import user
import os
import requests



def operation_endpoints(app,route_api):    
    @app.route(route_api+'/operations/cost/<type_>', methods=["POST"])
    def getOperations_by_type(type_):
        res = calculator.getOperations_by_type_(type_)
        try: 
            response = {'cost': res['cost']}
        except KeyError:
            response={ 'message': 'Operation not found'}
        except ValueError:
            response={ 'message': 'Operation not found'}
        except TypeError:
            response={ 'message': 'Operation not found'}
        return response


    @app.route(route_api+'/operations', methods=["POST"])
    def getOperations():
        res = calculator.getOperations_()
        return res

    
    @app.route(route_api+'/checkbalance', methods=["POST"])
    def checkBalance():
        try:
            operation = request.json.get('operation')
            user_id = request.json.get('user_id')
        except KeyError:
            response={ 'message': 'Operation not found'}
            return response
        except ValueError:
            response={ 'message': 'Operation not found'}
            return response
        except TypeError:
            response={ 'message': 'Operation not found'}
            return response

        response = calculator.checkBalance_(operation, user_id)
        return response


    @app.route(route_api+'/records_total', methods=["POST"])
    def getRecordsTotal():
        try:
            user_id = int(request.json.get('user_id'))
        except ValueError:
            response = jsonify({'msg': 'Bad parameters'})
            return response, 400
        except TypeError:
            response = jsonify({'msg': 'Bad parameters'})
            return response, 400

        res = calculator.getTotalRecords(user_id)
        return { 'total': res }


    @app.route(route_api+'/records', methods=["POST"])
    def getRecords():
        try:
            user_id = int(request.json.get('user_id'))
            page = int(request.json.get('page'))
            elements_peer_page = int(request.json.get('elements_peer_page'))
        except ValueError:
            response = jsonify({'msg': 'Bad parameters'})
            return response, 400
        except TypeError:
            response = jsonify({'msg': 'Bad parameters'})
            return response, 400
        
        order_field = request.json.get('order_field')
        if order_field is None:
            return {'msg': 'Bad parameters'}

        order = request.json.get('order')
        if order is None:
            response = jsonify({'msg': 'Bad parameters'})
            return response, 400

        res = calculator.getRecords_(user_id, page, order_field, order, elements_peer_page)
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
            
        except ValueError:
            response =  jsonify({'message': 'ValueError is not a int or float'})
            return response, 400
        except TypeError:
            response =  jsonify({'message': 'TypeError is not a int or float'})
            return response, 400

        if( type(v1) not in [int,float] or type(v2) not in [int,float]):
            response =  jsonify({'message': 'Error is not a int or float'})
            return response, 400
        
        rbalance = calculator.checkBalance_(operation,user_id)
        if rbalance["check"]:
            response = calculator.sum_(v1,v2, user_id, operation)
        else:
            response = {'message': 'Credit not enough'}

        return response

    
    @app.route(route_api+'/sub', methods=["POST"])
    def sub():
        try:
            v1 = float(request.json.get('v1'))
            v2 = float(request.json.get('v2'))
            user_id = int(request.json.get('user_id'))
            operation = 'substraction'
            
        except ValueError:
            response =  jsonify({'message': 'ValueError is not a int or float'})
            return response, 400
        except TypeError:
            response =  jsonify({'message': 'TypeError is not a int or float'})
            return response, 400

        if( type(v1) not in [int,float] or type(v2) not in [int,float]):
            response =  jsonify({'message': 'Error is not a int or float'})
            return response, 400
        
        rbalance = calculator.checkBalance_(operation,user_id)
        if rbalance["check"]:
            response = calculator.sub_(v1,v2, user_id, operation)
        else:
            response = {'message': 'Credit not enough'}
            
        return response


    @app.route(route_api+'/mult', methods=["POST"])
    def mult():
        try:
            v1 = float(request.json.get('v1'))
            v2 = float(request.json.get('v2'))
            user_id = int(request.json.get('user_id'))
            operation = 'multiplication'

        except ValueError:
            response =  jsonify({'message': 'ValueError is not a int or float'})
            return response, 400
        except TypeError:
            response =  jsonify({'message': 'TypeError is not a int or float'})
            return response, 400

        rbalance = calculator.checkBalance_(operation,user_id)
        if rbalance["check"]:
            response = calculator.mult_(v1,v2, user_id, operation)
        else:
            response = {'message': 'Credit not enough'}
            
        return response


    @app.route(route_api+'/div', methods=["POST"])
    def div():
        try:
            v1 = float(request.json.get('v1'))
            v2 = float(request.json.get('v2'))
            user_id = int(request.json.get('user_id'))
            operation = 'division'
        except ValueError:
            response =  jsonify({'message': 'ValueError is not a int or float'})
            return response, 400
        except TypeError:
            response =  jsonify({'message': 'TypeError is not a int or float'})
            return response, 400

        rbalance = calculator.checkBalance_(operation,user_id)
        if rbalance["check"]:
            response = calculator.div_(v1,v2, user_id, operation)
        else:
            response = {'message': 'Credit not enough'}
            
        return response


    @app.route(route_api+'/square_root', methods=["POST"])
    def square_root():
        try:
            v1 = float(request.json.get('v1'))
            user_id = int(request.json.get('user_id'))
            operation = 'square_root'
        except ValueError:
            response =  jsonify({'message': 'ValueError is not a int or float'})
            return response, 400
        except TypeError:
            response =  jsonify({'message': 'TypeError is not a int or float'})
            return response, 400

        if (v1 < 0):
            response =  jsonify({'message': 'Need a positive value'})
            return response, 400

        rbalance = calculator.checkBalance_(operation,user_id)
        if rbalance["check"]:
            response = calculator.square_root_(v1, user_id, operation)
        else:
            response = {'message': 'Credit not enough'}
            
        return response

    @app.route(route_api+'/random_string', methods=["POST"])
    def rand_string():
        url_random_org_string='https://api.random.org/json-rpc/2/invoke'
        try:
            user_id = int(request.json.get('user_id'))
            operation = 'random_string'
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

        rbalance = calculator.checkBalance_(operation,user_id)
        if rbalance["check"]:
            response = calculator.rand_str_(user_id, operation,result)
        else:
            response = {'message': 'Credit not enough'}
            
        return response