import sqlite3

db = sqlite3.connect('database.db', 10.0, check_same_thread=False)


def auth(login: str, password: str):
    res = db.execute(
        """SELECT * FROM users WHERE login = ? AND password = ?""",
        (login, password,)
    )

    if res.fetchone() is None:
        return None
    
    return login


def get_user_lessons(login: str, day: str):
    user_class = get_user_class_by_login(login)
    # req = 'SELECT * FROM ' + day + ' ' + 'WHERE class = ' + user_class
    # print(req)
    if day == 'Monday': res = db.execute("""SELECT * FROM Monday WHERE class = ?""", (user_class, ))
    if day == 'Tuesday': res = db.execute("""SELECT * FROM Tuesday WHERE class = ?""", (user_class, ))
    if day == 'Wednesday': res = db.execute("""SELECT * FROM Wednesday WHERE class = ?""", (user_class, ))
    if day == 'Thursday': res = db.execute("""SELECT * FROM Thursday WHERE class = ?""", (user_class, ))
    if day == 'Friday': res = db.execute("""SELECT * FROM Friday WHERE class = ?""", (user_class, ))
    if day == 'Saturday': res = db.execute("""SELECT * FROM Saturday WHERE class = ?""", (user_class, ))
    lessons = res.fetchone()
    
    if lessons is None:
        return None
    
    return lessons

def get_user_class_by_login(login: str):
    res = db.execute(
        """ SELECT * FROM users WHERE login = ?""",
        (login, )
    )

    # if res.fetchone() is None:
    #     return None
    
    return res.fetchone()[3]

def get_user_access_by_login(login: str):
    res = db.execute("""SELECT * FROM users WHERE login = ?""",
        (login, )
    )

    # if res.fetchone() is None:
    #     return None
    
    return res.fetchone()[4]


print(get_user_lessons('nikita', 'Friday'),
      get_user_access_by_login('nikita'))