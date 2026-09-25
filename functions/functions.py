import json
import os

appDir = os.path.join(
    os.environ["LOCALAPPDATA"],
    "ToDoList"
)

os.makedirs(appDir, exist_ok=True)

fileName = os.path.join(appDir, "tasks.json")


def loadTasks():
    if not os.path.exists(fileName):
        return []

    with open(fileName, "r", encoding="utf-8") as file:
        return json.load(file)
    
def saveTasks(tasks):
    with open(fileName, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)