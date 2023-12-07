import psycopg2 as psg
from datetime import date
import hashlib

conn = psg.connect(database="delivery_base", user='postgres', password='Seregungero204', port="5433")
cursor = conn.cursor() 
# cursor.execute("Select * FROM users")
# conn.commit()
# print(cursor.fetchall())

def session(email, password):
    cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, get_pass(password), ))
    conn.commit()
    print(cursor.query)
    if (cursor.fetchone() == None):
        return "Такого пользователя не существует"
    cursor.execute("SELECT * FROM orders WHERE user_email = %s", (email,))
    conn.commit()
    return cursor.fetchall()

def get_pass(inp):
    return hashlib.sha256(bytes(inp.encode('utf-8'))).hexdigest()
