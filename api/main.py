from fastapi import FastAPI
from pydantic import BaseModel

class Travel(BaseModel):
    departures: str | None = None
    date_departures: str | None = None
    arrivals: str | None = None
    date_arrivals: str | None = None    
    price_travel: float

app = FastAPI()

@app.get("/")
async def home():
    return {"Travel": len(travels)}

@app.get("/travels/{id_travel}")
async def search_for_trip(id_travel: int):
    if id_travel in travels:
        return travels[id_travel]
    else:
        return {"error": "id_travel not found"}

