from pydantic import BaseModel
import datetime

# Prediction 기본 양식
class PredictionInputBase(BaseModel):
    HomePlanet: str
    CryoSleep: bool
    Destination: str
    Age: float
    VIP: bool
    RoomService: float
    FoodCourt: float
    ShoppingMall: float
    Spa: float
    VRDeck: float
    deck: str
    deck_num: int
    deck_side: str
    group_number: int
    RoomService_cat: bool
    FoodCourt_cat: bool
    ShoppingMall_cat: bool
    Spa_cat: bool
    VRDeck_cat: bool


# DataBase에 넣을 양식
class PredictionCreate(PredictionInputBase):
    id: str
    Date: datetime.datetime
    Transported: bool
    Transported_prediction: bool

    class Config:
        orm_mode = str
