from psycopg2.extras import DictRow

from core.db_settings import execute_query


async def add_new_car():
    title: str = input("Title: ")
    color: str = input("Color: ")
    price: int = int(input("Price: "))
    query = "INSORT INTO cars(title,color,price) VALUES (%s,%s,%s)"
    params: tuple[str, str, int] = (title, color, price,)
    if execute_query(query=query, params=params):
        print("Car added")
    print("Something went wrong, try again later.")


async def get_all_cars():
    query = "SELECT * FROM cars"
    all_cars: DictRow = execute_query(query=query, fetch="all")
    if all_cars:
        return all_cars
    else:
        print("No cars yet.")
        return False

def show_all_cars(all_cars:dict):
    if not all_cars:
        return False
    for car in all_cars:
        print(f"| Id: {car['id']} | Title: {car['title']} | Color: {car['color']}")
    return True

