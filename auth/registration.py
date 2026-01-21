from core.db_settings import execute_query
from core.config import admin_user_name,admin_password
import asyncio

active_user = dict()


async def register() -> bool:
    """
    Register new users
    :return: True if success else False
    """
    username: str = input("Username: ")
    # check email if exists or not
    # query: str = "SELECT * FROM users WHERE username=%s"
    # params: tuple[str] = (username,)
    # if execute_query(query=query, params=params):
    #     print("Username already exists!")
    #     return register()
    phone:str = input("Phone: ")
    password: str = input("Password: ")

    query: str = "INSERT INTO users (username,phone, password) VALUES (%s,%s, %s)"
    params: tuple[str,str, str] = (username,phone, password,)

    if execute_query(query=query, params=params):
        print("Successfully done, you can login now")
        return True
    else:
        print("Something went wrong, try again later")
        return False


async def login() -> bool | str:
    username: str = input("Username: ")
    password: str = input("Password: ")

    if username == admin_user_name and password == admin_password:
        return "admin"

    query: str = "SELECT id, username, phone FROM users WHERE username=%s AND password=%s"
    params: tuple[str, str] = (username, password,)

    user_in = execute_query(query=query, params=params, fetch="one")
    if user_in:
        global active_user
        active_user = dict(user_in)
        return "user"
    return False


