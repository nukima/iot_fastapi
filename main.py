from typing import Union
from fastapi import FastAPI
# fix ObjectId & FastApi conflict
import pydantic
from pydantic import BaseModel
from bson.objectid import ObjectId
pydantic.json.ENCODERS_BY_TYPE[ObjectId]=str
import database
import mqtt_connect
from predict_ppm import predict_ppm

class predictRequestEntity(BaseModel):
    time: int
    co: float
    alcohol: float
    co2: float
    toluen: float
    nh4: float
    aceton: float
    ppm: float
    temperature: float
    humidity: float

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Welcome To The Hell :)"}


# get 2 last record
@app.get("/latest")
def get_latest():
    latest_records = database.mongodb_collection.find().sort("_id", -1).limit(3)
    print(latest_records)
    latest_records = list(latest_records)
    return latest_records

# led remote
# 0: green, 1: orange, 2: red
@app.get("/led/")
def led_control(led_status: int):
    if led_status == 0:
        mqtt_connect.send_led_status(0)
        return {"message": "LED is green"}
    elif led_status == 1:
        mqtt_connect.send_led_status(1)
        return {"message": "LED is orange"}
    elif led_status == 2:
        mqtt_connect.send_led_status(2)
        return {"message": "LED is red"}

# predict ppm
@app.post("/predict")
def predict(data: predictRequestEntity):
    data = data.dict()
    print(data)
    print(type(data))
    prediction = predict_ppm(data)
    return {"ppm_prediction": prediction}
    

    

