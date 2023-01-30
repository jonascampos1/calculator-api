# calculator-api-app

This api is created with Flask and Python

## Recommended IDE Setup

[PyCharm](https://www.jetbrains.com/es-es/pycharm/)

## Installation with Docker
You need to install docker on your computer

## First - Project Setup
Navigate to the app project folder and execute
	
```sh
docker compose up
```

## Second - Open new terminal and navigate to project folder and execute:

```sh
docker exec -u root -it calculator sh
```

## Third - Initialize DB
Execute:
	cd /home/app
```sh
cd /home/app
python init_db.py
```

### This add the tables content necessary for work
## Table Operation
```sh
 id | type           | cost |
+----+----------------+------+
|  1 | addition       |    1 |
|  2 | substraction   |    2 |
|  3 | multiplication |    3 |
|  4 | division       |    4 |
|  5 | square_root    |    5 |
|  6 | random_string  |    6 |
```

## Table User
```sh
+----------+-------------+------+-----+---------+----------------+
| Field    | Type        | Null | Key | Default | Extra          |
+----------+-------------+------+-----+---------+----------------+
| id       | int         | NO   | PRI | NULL    | auto_increment |
| username | varchar(30) | YES  |     | NULL    |                |
| password | varchar(50) | YES  |     | NULL    |                |
| status   | smallint    | YES  |     | NULL    |                |
| balance  | float       | YES  |     | NULL    |                |
+----------+-------------+------+-----+---------+----------------+
```

## Table Record
```sh
+--------------------+-------------+------+-----+---------+----------------+
| Field              | Type        | Null | Key | Default | Extra          |
+--------------------+-------------+------+-----+---------+----------------+
| id                 | int         | NO   | PRI | NULL    | auto_increment |
| operation_id       | int         | YES  |     | NULL    |                |
| user_id            | int         | YES  |     | NULL    |                |
| amount             | float       | YES  |     | NULL    |                |
| user_balance       | float       | YES  |     | NULL    |                |
| operation_response | varchar(30) | YES  |     | NULL    |                |
| date               | datetime    | YES  |     | NULL    |                |
| deletedAt          | datetime    | YES  |     | NULL    |                |
+--------------------+-------------+------+-----+---------+----------------+
```
### 



### Include 2 users to access login with this values(password is hashed on DB)

```sh
username: test1@test.com
password: aB12345@

username: test2@test.com
password: aB12345#
```

You are ready to use this backend project

# API Documentation

## Endpoint Addition method POST
### /api/v1/sum
Description: Sum two values rest credit balance and insert a Record 

Required JSON Object example
```sh
{
    "v1": "3",
    "v2": "2",
    "user_id": 1
}
```
Response JSON Object example
```sh
{
    "cost": 1.0,
    "result": 5.0,
    "user_balance": 5
}
```


## Endpoint Substraction method POST
### /api/v1/sub
Description: Substract two values rest credit balance and insert a Record 

Required JSON Object example
```sh
{
    "v1": "3",
    "v2": "2",
    "user_id": 1
}
```
Response JSON Object example
```sh
{
    "cost": 1.0,
    "result": 1.0,
    "user_balance": 5
}
```

## Endpoint Multiplication method POST
### /api/v1/mult
Description: Multiply two values rest credit balance and insert a Record 

Required JSON Object example
```sh
{
    "v1": "3",
    "v2": "2",
    "user_id": 1
}
```
Response JSON Object example
```sh
{
    "cost": 1.0,
    "result": 6.0,
    "user_balance": 5
}
```

## Endpoint Division method POST
### /api/v1/div
Description: Divide two values rest credit balance and insert a Record 

Required JSON Object example
```sh
{
    "v1": "3",
    "v2": "2",
    "user_id": 1
}
```
Response JSON Object example
```sh
{
    "cost": 1.0,
    "result": 5.0,
    "user_balance": 5
}
```

## Endpoint Square Root method POST
### /api/v1/square_root
Description: Get the square root of one value, rest credit balance and insert a Record 

Required JSON Object example
```sh
{
    "v1": "9",
    "user_id": 1
}
```
Response JSON Object example
```sh
{
    "cost": 1.0,
    "result": 3.0,
    "user_balance": 5
}
```

## Endpoint Random String method POST
### /api/v1/sum
Description: Get a random string of 8 characters

Required JSON Object example
```sh
{
    "user_id": 1
}
```
Response JSON Object example
```sh
{
    "cost": 6.0,
    "result": "N#CYIzh&",
    "user_balance": 24.0
}
```

## Endpoint Login method POST
### /api/v1/sum
Description: Authorize user access

Required JSON Object example
```sh
{
    "username": "test1@test.com",
    "password": "aB12345@"
}
```
Response JSON Object example success auth
```sh
{
    "balance": 30.0,
    "msg": "Auth Success",
    "user_id": 1,
    "username": "test1@test.com"
}
```
Response JSON Object example failure auth
```sh
{
    "msg": "Auth Failure"
}
```

## Endpoint get cost for a operation method POST
### /api/v1/operations/cost/<operation>
Description: Get the cost of an operation by his name
Posible values: addition, substraction, division, multiplication, random_string, square_root

Response JSON Object example
```sh
{
    "cost": 5.0
}
```
	
## Endpoint Delete Record by id method DELETE
### api/v1/records/<id>
Description: Soft Delete a record by his id
	

Response JSON Object example
```sh
{
    "message": "Deleted id: <id> "
}
```

## Endpoint get Records of a user method POST
### api/v1/records
Description: Get records from an user with pagination

Request JSON Object example
```sh
{
    "user_id": "1",
    "page": "1",
    "elements_peer_page": "10",
    "order_field": "id",
    "order": "desc"
}
```

Response JSON Object example
```sh
[
    {
        "amount": 6.0,
        "date": "2023-01-30 06:38",
        "deletedAt": null,
        "id": 1,
        "operation_id": 6,
        "operation_response": "N#CYIzh&",
        "user_balance": 24.0,
        "user_id": 1
    }
]
```
	
## Endpoint Check balance of a user against the operation cost to get method POST
### /api/v1/checkbalance
Description: Verify the balance and the operation cost if have enough balance get true
	

Request JSON Object example
```sh
{
    "operation": "addition",
    "user_id": "1"
}
```
	
Response JSON Object example
```sh
{
    "check": true
}
```

## Endpoint get total records for pagination method POST
### /api/v1/records_total
Description: Verify the balance and the operation cost if have enough balance get true
	

Request JSON Object example
```sh
{
    "user_id": "1"
}
```
	
Response JSON Object example
```sh
{
    "total": 11
}
```

