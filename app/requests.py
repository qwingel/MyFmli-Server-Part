from flask import Blueprint, request, session
from app.db import auth, get_user_class_by_login, get_user_access_by_login, get_user_lessons

module = Blueprint("main", __name__, url_prefix="/")


@module.post("/")
def index():
    if "username" in session:
        return {
            "status" : "OK",
            "message": f"{session['username']}"
        }
    
    return {
        "status": "OK",
        "message": "Войдите в систему",
    }


@module.post("/login")
def login():
    data = request.get_json()
    if auth(data["login"], data["password"]) is None:
        return {
            "status": "Неверный логин или пароль",
            "message": "failed",
        }
    session["username"] = data["login"]
    print(session)
    return {
        "status": "Вы вошли в систему",
        "message": data["login"],
    }


@module.get("/logout")
def logout():
    session.clear()
    return {
        "status": "accepted",
        "message": "Вы вышли из системы",
    }


@module.post("/class")
def classes():
    data = request.get_json()
    return {
        "status":"OK",
        "message": get_user_class_by_login(data["login"])
    }


@module.post("/access")
def access():
    data = request.get_json()
    return {
        "status": "OK",
        "message": get_user_access_by_login(data["login"])
    }


@module.post("/lessons")
def lessons():
    data = request.get_json()
    print(data)
    print(session)
    if "username" not in session:
        return {
            "status": "OK",
            "message": "Войдите в систему",
            "data": []
        }
    
    user_login = session["username"]
    return {
        "status": "OK", 
        "message": "",
        "data": get_user_lessons(user_login, data)
    }

