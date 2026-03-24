from fastapi import FastAPI
from pydantic import BaseModel
from features.task_sync import add_task

app = FastAPI()

# request model
class Task(BaseModel):
    cmd: str


@app.get("/")
def home():
    return {"status": "Aria server running 💕"}


@app.post("/task")
def create_task(task: Task):
    add_task(task.cmd)
    return {"message": f"Task added: {task.cmd}"}