from flask import request, jsonify
import re
from services.user import create_user
import services.user as user_service
import hashlib




def user_endpoints(app,route_api):


    @app.route(route_api + 'user', methods=['POST'])
    def create():
        username = request.json.get('username')
        password = request.json.get('password')

        if not re.match("^[a-zA-Z]{1,30}$", username):
            response = jsonify({'msg': 'Bad parameters', 'status_code': '400'})
            return response, 400

        if not re.match("^[0-9]{30}$", password):
            response = jsonify({'msg': 'Bad parameters', 'status_code': '400'})
            return response, 400

        if user_service.verify_user_exist(username):
            response = jsonify({'msg': 'User exists, change username'})
            return response, 401

        
        password_hashed = hashlib.md5(password.encode('utf-8')).hexdigest()

        user_new = {
            "username": username,
            "password": password_hashed,
            "active": 0 #active default 0
        }

        r = create_user(user_new)
        return {'User created': f'{r}:yes'}
