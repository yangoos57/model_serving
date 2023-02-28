from sqlalchemy import Column, DateTime, BOOLEAN, FLOAT, INTEGER, String

from sqlalchemy.sql import func
from db.database import Base


class Prediction(Base):
    __tablename__ = "prediction_table"

    id = Column(String(120), primary_key=True)
    Date = Column(DateTime, index=True, server_default=func.now())
    HomePlanet = Column(String(10))
    CryoSleep = Column(BOOLEAN)
    Destination = Column(String(15))
    Age = Column(FLOAT)
    VIP = Column(BOOLEAN)
    RoomService = Column(FLOAT)
    FoodCourt = Column(FLOAT)
    ShoppingMall = Column(FLOAT)
    Spa = Column(FLOAT)
    VRDeck = Column(FLOAT)
    deck = Column(String(1))
    deck_num = Column(INTEGER)
    deck_side = Column(String(1))
    group_number = Column(INTEGER)
    RoomService_cat = Column(BOOLEAN)
    FoodCourt_cat = Column(BOOLEAN)
    ShoppingMall_cat = Column(BOOLEAN)
    Spa_cat = Column(BOOLEAN)
    VRDeck_cat = Column(BOOLEAN)
    Transported = Column(BOOLEAN)
    Transported_prediction = Column(BOOLEAN, default="")
