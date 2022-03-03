import sqlite3
import random

con = sqlite3.connect("user.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
    login TEXT,
    password TEXT,
    cash INT
)""")
con.commit()


def reg():
    global user_login
    user_login = input("Input login: ")
    user_password = input("Input password: ")
    cur.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if cur.fetchone() is None:
        cur.execute("INSERT INTO users VALUES(?, ?, ?)", (user_login, user_password, 0))
        con.commit()
        print("Completed")
        menu()
    else:
        print("This login already exists, try again")
        reg()


def money():
    cur.execute(f"SELECT cash FROM users WHERE login = '{user_login}'")
    return cur.fetchone()[0]


def menu():
    m = money()
    print("Choose game:\none of three -- n\nmore or less -- mol\nto quite -- q\nshow money -- cash\n")
    game = input()
    if game == "n":
        one_of_three()
    elif game == "mol":
        if m >= 5:
            more_or_less()
        else:
            print("You must have 5$\n")
            menu()
    elif game == "cash":
        print(f"{m}$\n")
        menu()
    elif game == "q":
        pass
    else:
        print("No such option\n")
        menu()


def one_of_three():
    num = random.randint(1, 3)
    guess = int(input("Guess number from one to three: "))
    m = money()
    if guess == num:
        print("You win!")
        cur.execute(f"UPDATE users SET cash = '{m + 5}' WHERE login = '{user_login}'")
        con.commit()
        menu()
    elif guess > 3 or guess < 1:
        print("Don't use numbers which more than 3 or less than 1")
        one_of_three()
    else:
        print("You lose")
        menu()


def more_or_less():
    first = random.randint(1, 100)
    guess = input("Next number will be more, less or equally (m, l, e): ")
    second = random.randint(1, 100)
    m = money()
    if guess == "m":
        if second > first:
            print("You win!")
            cur.execute(f"UPDATE users SET cash = '{m + 10}' WHERE login = '{user_login}'")
            con.commit()
            menu()
        else:
            print("You lose")
            cur.execute(f"UPDATE users SET cash = '{m - 5}' WHERE login = '{user_login}'")
            con.commit()
            menu()
    elif guess == "l":
        if second < first:
            print("You win!")
            cur.execute(f"UPDATE users SET cash = '{m + 10}' WHERE login = '{user_login}'")
            con.commit()
            menu()
        else:
            print("You lose")
            cur.execute(f"UPDATE users SET cash = '{m - 5}' WHERE login = '{user_login}'")
            con.commit()
            menu()
    elif guess == "e":
        if second == first:
            print("You win!")
            cur.execute(f"UPDATE users SET cash = '{m + 20}' WHERE login = '{user_login}'")
            con.commit()
            menu()
        else:
            print("You lose")
            cur.execute(f"UPDATE users SET cash = '{m - 5}' WHERE login = '{user_login}'")
            con.commit()
            menu()
    else:
        print("No such option")
        more_or_less()


reg()
