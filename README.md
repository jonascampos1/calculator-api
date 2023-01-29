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

### 

```sh
npm run test:unit
```

### Include 2 users to access login with this values(password is hashed on DB)

```sh
username: test1@test.com
password: aB12345@

username: test2@test.com
password: aB12345#
```

You are ready to use this backend project