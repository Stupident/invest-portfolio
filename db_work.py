import sqlite3

def add_user(login, email, pswrd):
    conn = sqlite3.connect('db/database.db')
    cur = conn.cursor()
    resp = False
    try:
        cur.execute('INSERT INTO users (login, email, pswrd, deposit) VALUES (?, ?, ?, 0)',
                       (login, email, pswrd))
        cur.close()
        conn.commit()
    except Exception as e:
        print(e)
        if str(e).find("email") != -1:
            resp = ''.join(["User with email \"", email, "\" already exist"])
        elif str(e).find("login") != -1:
            resp = ''.join(["Login \"", login, "\" is already taken"])
        else:
            resp = "We have some troubles :(\nTry later"
    print(resp)
    return(resp)

def find_user(login, pswrd):
    conn = sqlite3.connect('db/database.db')
    cur = conn.cursor()
    resp = False
    user_pswrd = ''
    try:
        cur.execute('SELECT pswrd FROM users WHERE login = ? OR email = ?', (login, login))
        user_pswrd = cur.fetchone()
        cur.close()
        conn.commit()
    except Exception as e:
        print(e)
        resp = "We have some troubles :(\nTry later"
    if user_pswrd == None:
        resp = "User with this login or email not exists"
    elif user_pswrd[0] != pswrd:
        resp = "Wrong password"

    return(resp)


def get_invests(login):
    conn = sqlite3.connect('db/database.db')
    cur = conn.cursor()
    resp = False
    user_invests = None
    try:
        cur.execute('SELECT currency, amount, price, value FROM invests WHERE user_login = ? ', (login,))
        user_invests = cur.fetchall()
        print("DBDBDBD")
        print(user_invests)
        cur.close()
        conn.commit()
    except Exception as e:
        print(e)
        resp = "We have some troubles :(\nTry later"
    if user_invests == None:
        resp = "Add your first assets"
    else:
        resp = user_invests

    print(resp)
    return (resp)

def add_assets(login, title, amount, price):
    value = float(amount)*float(price)
    conn = sqlite3.connect('db/database.db')
    cur = conn.cursor()
    resp = False
    try:
        cur.execute('INSERT INTO invests (user_login, currency, amount, price, value) VALUES (?, ?, ?, ?, ?)',
                       (login, title, amount, price, str(value)))
        cur.execute('SELECT deposit FROM users WHERE login=?', (login,))
        dep = float(cur.fetchone()[0]) + value
        cur.execute('UPDATE users SET deposit = ? WHERE login = ?', (dep, login))
        cur.close()
        conn.commit()
    except Exception as e:
        print(e)
        resp = "We have some troubles :(\nTry later"
    print(resp)
    return(resp)