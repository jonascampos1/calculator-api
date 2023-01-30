from models.user import userTable
from config.db import conn
import hashlib


def auth_user(username, password):
    res = conn \
        .execute(userTable
                 .select()
                 .where(userTable.c.username == username)) \
        .first()

    if res is None:
        return {'auth': 0,
                'username': '',
                'user_id': ''
                }
    else:
        
        password_hashed = hashlib.md5(password.encode('utf-8')).hexdigest()
        if username == res.username and password_hashed == res.password:
            return {'auth': 1,
                    'username': res.username,
                    'user_id': res.id,
                    'balance': res.balance
                    }
        else:
            return {'auth': 0}
