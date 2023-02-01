from config.pymysql_db import connect_mysql
from flask import Flask, jsonify
import os
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)

route_api=os.getenv('ROUTE_API')

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

    response = getBalance2(id)
    return {'balance': response }



def getBalance2(id):
    connection = connect_mysql()
    with connection:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `balance` FROM `User` WHERE `id`=%s"
            cursor.execute(sql, (id))
            result = cursor.fetchone()
            cursor.close()

    return int(result['balance'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)