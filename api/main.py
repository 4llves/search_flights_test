from fastapi import FastAPI
from pydantic import BaseModel

class Travel(BaseModel):
    departures: str | None = None
    date_departures: str | None = None
    arrivals: str | None = None
    date_arrivals: str | None = None    
    price_travel: float

app = FastAPI()

travels = {
    1: {
        "input_departures": "BEL",
        "date_departure": "14/03/2024",
        "input_arrivals": "GRU",
        "date_arrivals": "20/03/2024",
        "value_travels": 1000,
    },
    2: {
        "input_departures": "CGH",
        "date_departure": "23/03/2024",
        "input_arrivals": "GIG",
        "date_arrivals": "29/03/2024",
        "value_travels": 2000,
    }
}

@app.get("/")
async def home():
    return {"Travel": len(travels)}

@app.get("/travels/{id_travel}")
async def search_for_trip(id_travel: int):
    return travels[id_travel]

