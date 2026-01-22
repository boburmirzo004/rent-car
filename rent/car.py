import logging

from psycopg2.extras import DictRow

from core.db_settings import execute_query

logger=logging.getLogger(__name__)

async def add_new_car():
    title: str = input("Title: ")
    color: str = input("Color: ")
    price: int = int(input("Price: "))

    query = "INSERT INTO cars(title,color,price) VALUES (%s,%s,%s)"
    params: tuple[str, str, int] = (title, color, price,)
    if execute_query(query=query, params=params):
        logger.info(msg="Car added.")
        print("Car added")
        return True
    print("Something went wrong, try again later.")
    return False


async def get_all_cars():
    query = "SELECT * FROM cars"
    all_cars: DictRow = execute_query(query=query, fetch="all")

    if all_cars:
        return all_cars
    else:
        logger.warning(msg="No cars yet.")
        print("No cars yet.")
        return False


def show_all_cars(all_cars: dict):
    if not all_cars:
        return False

    for car in all_cars:
        print(f"| Id: {car['id']} | Title: {car['title']} | Color: {car['color']}")
    return True
