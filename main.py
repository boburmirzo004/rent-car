import datetime

from psycopg2.extras import DictRow

from core.db_settings import execute_query
import asyncio
from auth.registration import register, login,active_user
from rent.rent import create_an_order, finishing_order, show_all_active_orders, show_all_orders, deactivate_car
from rent.car import add_new_car, get_all_cars, show_all_cars
from core.db_settings import execute_query
from core.config import admin_user_name, admin_password
from rent.user import show_all_my_orders
from utils.menus import auth_menu, admin_menu, user_menu

async def auth_menu_func():
    print(auth_menu)
    choice = input("Enter choice: ")

    if choice == "1":
        await register()
        return await auth_menu_func()

    elif choice == "2":
        login_success = await login()
        if not login_success:
            print("Login failed")
            return await auth_menu_func()
        if login_success=="admin":
            return await show_admin_menu()
        elif login_success=="user":
            return await show_user_menu()
    elif choice == "3":
        print("Goodbye!")
        return False
    else:
        print("Invalid choice.")
        return await auth_menu_func()


# ---------------- Admin Menu ----------------
async def show_admin_menu():
    print(admin_menu)
    choice = input("Admin choice: ")

    if choice == "1":
        cars = await get_all_cars()
        show_all_cars(cars)
        return await show_admin_menu()

    elif choice == "2":
        success = await add_new_car()
        if success:
            print("Car added successfully!")
        else:
            print("Failed to add car.")
        return await show_admin_menu()

    elif choice == "3":
        cars = await get_all_cars()
        success = await deactivate_car(cars)
        if success:
            print("Car deactivated.")
        else:
            print("Failed to deactivate car.")
        return await show_admin_menu()

    elif choice == "4":
        success = await create_an_order()
        if success:
            print("Order created!")
        else:
            print("Failed to create order.")
        return await show_admin_menu()

    elif choice == "5":
        success = await show_all_active_orders()
        if not success:
            print("No active orders.")
        return await show_admin_menu()

    elif choice == "6":
        success = await show_all_orders()
        if not success:
            print("No orders found.")
        return await show_admin_menu()

    elif choice == "7":
        today = datetime.date.today()
        success = await finishing_order(today)
        if success:
            print("Order finished successfully.")
        else:
            print("Failed to finish order.")
        return await show_admin_menu()

    elif choice == "8":
        return await auth_menu_func()  # logout

    else:
        print("Invalid choice.")
        return await show_admin_menu()


# ---------------- User Menu ----------------
async def show_user_menu():
    print(user_menu)
    choice = input("User choice: ")

    if choice == "1":
        cars = await get_all_cars()
        show_all_cars(cars)
        return await show_user_menu()

    elif choice == "2":
        success= await show_all_my_orders()
        return await show_user_menu()

    elif choice == "3":
        return await auth_menu_func()  # logout

    else:
        print("Invalid choice.")
        return await show_user_menu()


# ---------------- Main ----------------
if __name__ == "__main__":
    asyncio.run(auth_menu_func())

