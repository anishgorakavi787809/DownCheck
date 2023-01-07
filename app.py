from fastapi import FastAPI
from pydantic import *
import uvicorn

app = FastAPI()

class Timex(BaseModel):
    day: int | None = 0
    hour: int | None = 0
    min: int | None = 0
    sec: int | None = 0
@app.get("/")
def index():
    return {"Roar":"I'm running"}

@app.post("/every_time")
def everyX(arg:Timex):
    day_sec = arg.day * 24 * 3600
    hour_sec = arg.hour * 3600
    min_sec = arg.min * 60
    totsec = day_sec + hour_sec + min_sec + arg.sec
    return totsec

uvicorn.run(app,port=80)