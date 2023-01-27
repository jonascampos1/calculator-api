from flask import Flask
import os
from controllers import calculator, auth, user
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

auth.auth_endpoints(app, os.getenv('ROUTE_API'))
user.user_endpoints(app, os.getenv('ROUTE_API'))
calculator.operation_endpoints(app, os.getenv('ROUTE_API'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
    