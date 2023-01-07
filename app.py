from fastapi import FastAPI
from pydantic import *
import uvicorn
from crontab import CronTab

app = FastAPI()
cron = CronTab(user=True)

class Timex(BaseModel):
    day: int | None = 0
    hour: int | None = 0
    min: int | None = 0
    sec: int | None = 0
    websites: list
@app.get("/")
def index():
    return {"Roar":"I'm running"}

@app.post("/create_task")
def everyX(arg:Timex):
    day = arg.day * 24 * 60
    hour = arg.hour * 60
    min = arg.min
    totmi = day + hour + min + arg.sec/60
    args = ""
    for i in arg.websites:
        args += i + " "
    job = cron.new(command=f"python3 /home/anish/Downtime/timex.py {args}")
    job.minute.every(totmi)
    cron.write()
    return "Yup, sceduled task!"

@app.delete("/all_tasks")
def ddel():
    return {"MEH"}
    
uvicorn.run(app,port=80)