from flask import request, jsonify
import re
from services.auth import auth_user



def auth_endpoints(app,route_api):
    @app.route(route_api + 'login', methods=['POST'])
    def login():
        username = request.json.get("username")
        password = request.json.get("password")

        if not re.match("^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", username):
            response = jsonify({'msg': 'Invalid email un username', 'status_code': '400'})
            return response, 400

        if not re.match("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", password):
            response = jsonify({'msg': 'Bad parameters on password must have min 8 characters, at least one uppercase English letter, at least one lowercase English letter, at least one digit, at least one special character', 'status_code': '400'})
            return response, 400

        response = auth_user(username, password)
        if response['auth'] == 1:
            return jsonify({'msg': 'Auth Success',
                            'username': response["username"],
                            'user_id': response["user_id"]
                            }), 200
        else:
            return jsonify({'msg': 'Auth Failure'}), 401