import os

url = os.getenv("DB_URL")
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")

print(user, password)


class Deployment:
    db_dir = f"mysql+pymysql://{user}:{password}@{url}:3306"
    db_name = "ML"
    columns = [
        "HomePlanet",
        "CryoSleep",
        "Destination",
        "Age",
        "VIP",
        "RoomService",
        "FoodCourt",
        "ShoppingMall",
        "Spa",
        "VRDeck",
        "deck",
        "deck_num",
        "deck_side",
        "group_number",
        "RoomService_cat",
        "FoodCourt_cat",
        "ShoppingMall_cat",
        "Spa_cat",
        "VRDeck_cat",
    ]


class Test:
    db_dir = f"mysql+pymysql://{user}:{password}@{url}:3306"
    db_name = "testML"
