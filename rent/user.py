import auth.registration
from core.db_settings import execute_query


async def show_all_my_orders():
    active_user=auth.registration.active_user
    orders = execute_query(
        query="SELECT * FROM orders WHERE user_id=%s",
        params=(active_user['id'],),
        fetch="all"
    )
    if orders:
        for order in orders:
            print(
                f"| Id: {order['id']} | Car id: {order['car_id']} | Rent: {order['rent_at']} | Return: {order['return_at']}")
    else:
        print("No orders found.")