from flask import request, jsonify
import re
from services.user import create_user, getBalance_
import services.user as user_service
import hashlib




def user_endpoints(app,route_api):



    @app.route(route_api + 'user', methods=['POST'])
    def create():
        username = request.json.get('username')
        password = request.json.get('password')

        if not re.match(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", username):
            response = jsonify({'msg': 'Bad parameters 1', 'status_code': '400'})
            return response, 400

        if not re.match("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", password):
            response = jsonify({'msg': 'Bad parameters 2', 'status_code': '400'})
            return response, 400

        if user_service.verify_user_exist(username):
            response = jsonify({'msg': 'User exists, change username'})
            return response, 401

        
        password_hashed = hashlib.md5(password.encode('utf-8')).hexdigest()

        user_new = {
            "username": username,
            "password": password_hashed,
            "active": 0, #active default 0
            "balance": 30
        }

        r = create_user(user_new)
        return {'User created': f'{r}:yes'}

    
    @app.route(route_api + 'userbalance/<id>', methods=['POST'])
    def getBalance(id):
        response = {}
        try:
            id = int(id)
        except ValueError:
            response = jsonify({'message': 'Expecting int'})
            return response, 400
        except TypeError:
            response = jsonify({'message': 'Expecting int'})
            return response, 400

        response = getBalance_(id)
        return {'balance': response }
