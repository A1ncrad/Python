import sqlite3


db = sqlite3.connect("user.db")
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS user(
    login TEXT,
    password TEXT, 
    cash INT
)""")

db.commit()

login_user = input("Type your login : ")
password_user = input("Type your password : ")

sql.execute(f"SELECT login FROM user WHERE login = '{login_user}'")
if sql.fetchone() is None:
    sql.execute(f"INSERT INTO user VALUES(?,?,?)", (login_user, password_user, 0))
    db.commit()
    print("Зарегестрированно")
else:
    print("Такая запись имеется")
    for i in sql.execute("SELECT * FROM user"):
        print(i)
        