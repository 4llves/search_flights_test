from fastapi import FastAPI
from pydantic import BaseModel


class Travel(BaseModel):
    departures: str | None = None
    date_departures: str | None = None
    arrivals: str | None = None
    date_arrivals: str | None = None    
    price_travel: float


app = FastAPI()


@app.post("/travel/")
async def create_item(travel: Travel):
    travel_dict = travel.dict()    
    return travel_dict
