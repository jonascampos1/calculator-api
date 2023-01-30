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
