import datetime
from turtledemo.clock import current_day

from psycopg2.extras import DictRow

from core.db_settings import execute_query
from rent.car import show_all_cars


async def show_all_users():
    query = "SELECT * FROM USERS"
    all_users: DictRow = execute_query(query=query, fetch="all")
    if all_users:
        for user in all_users:
            print(f"| Id: {user['id']} | User name: {user['username']} | Phone: {user['phone']}")
        return True
    else:
        print("No users yet")
        return False

async def deactivate_car(all_cars:dict):
    if show_all_cars(all_cars):
        choice:int=int(input("Enter ID: "))
        query="SELECT * FROM cars WHERE id=%s"
        params:tuple[int]=(choice,)
        if execute_query(query=query,params=params):
            query1="UPDATE cars SET deactivate=true WHERE id=%s"
            params1:tuple[int]=(choice,)
            if execute_query(query=query1,params=params1):
                print("Done")
                return True
        else:
            print("No such car found")
            return False
    return False

async def create_an_order():
    username:str=input("Username: ")
    phone:str=input("Phone: ")
    query="SELECT * FROM users WHERE username=%s AND phone=%s"
    params:tuple[str,str]=(username,phone,)
    user:DictRow=execute_query(query=query,params=params,fetch='one')
    if not user:
        print("No such user found.")
        return False
    if not user['is_active']:
        choice:int=int(input("Enter ID: "))
        query1="SELECT * FROM cars WHERE id=%s"
        params1:tuple[int]= (choice,)
        car:DictRow=execute_query(query=query1,params=params1,fetch="one")
        if not car:
            print("No such car found")
            return False
        if not car['is_active'] and car['deactivate']:
            query2="INSERT INTO orders (user_id,car_id,is_active) VALUES (%s,%s,%s)"
            params2:tuple[int,int,bool]=(user['id'],car['id'],True,)

            if execute_query(query=query2,params=params2):
                print("Thank you for your order.")
                return True
            return False
        else:
            print("This car is busy.")
            return False
    else:
        print("No such user exists.")
        return False


async def show_all_active_orders():
    query="SELECT * FROM orders WHERE is_active=true"
    all_orders:DictRow=execute_query(query=query,fetch="all")
    if not all_orders:
        print("No active orders.")
        return False
    for order in all_orders:
        print(f"|Id: {order['id']} | User id: {order['user_id']} | Car id: {order['car_id']} | Rent data: {order['rent_at']} |")
    return True



async def show_all_orders():
    query="SELECT * FROM orders"
    all_orders:DictRow=execute_query(query=query,fetch="all")
    if not all_orders:
        print("No active orders.")
        return False
    for order in all_orders:
        print(f"|Id: {order['id']} | User id: {order['user_id']} | Car id: {order['car_id']}")
    return True

async def finishing_order(current_date:datetime.date = None):
    username: str = input("Username: ")
    phone: str = input("Phone: ")
    query = "SELECT * FROM users WHERE username=%s AND phone=%s"
    params: tuple[str, str] = (username, phone,)
    user: DictRow = execute_query(query=query, params=params, fetch='one')
    if not user:
        print("No such user found.")
        return False

    query2="SELECT * FROM orders where user_id=%s AND is_active=%s"
    params2:tuple[int,bool] = (user['id'],True,)
    order:DictRow = execute_query(query=query2,params=params2,fetch="one")
    if not order:
        print("No such order.")
        return False
    query3="UPDATE orders SET is_active=%s , return_at=%s WHERE id =%s"
    params3:tuple[bool,datetime.date,int] = (False,current_date,order['id'])

    execute_query(query=query3, params=params3)
    print(f"Order {order['id']} finished on {current_date}.")
    return True
