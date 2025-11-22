from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# ----------------------------
# Room Class
# ----------------------------
class Room:
    def __init__(self, name, is_dirty, color):
        self.name = name
        self.is_dirty = is_dirty
        self.color = color

# ----------------------------
# Environment (4 Rooms)
# ----------------------------
class Environment:
    def __init__(self):
        self.rooms = [
            Room("Room 1", True, "#ff4d4d"),    # Dirty
            Room("Room 2", False, "#4CAF50"),   # Clean
            Room("Room 3", True, "#ff4d4d"),    # Dirty
            Room("Room 4", False, "#4CAF50")    # Clean
        ]
        self.agent_position = 0

    def current_room(self):
        return self.rooms[self.agent_position]

    def move_next(self):
        self.agent_position += 1

    def done(self):
        return self.agent_position >= len(self.rooms)

# ----------------------------
# Agent Logic
# ----------------------------
class SimpleAgent:
    def __init__(self, environment):
        self.env = environment

    def step(self):
        if self.env.done():
            return None
        room = self.env.current_room()
        log = ""
        if room.is_dirty:
            room.is_dirty = False
            log = f"Cleaned {room.name}"
        else:
            log = f"{room.name} already clean"
        self.env.move_next()
        return {
            "log": log,
            "room": {
                "name": room.name,
                "clean": not room.is_dirty,
                "color": room.color
            }
        }

# ----------------------------
# FastAPI App
# ----------------------------
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/ui")
def ui_page():
    return FileResponse("static/index.html")

@app.get("/")
def home():
    return {"message": "Vacuum Agent API Running Successfully"}

@app.get("/run-agent")
def run_agent():
    """
    Return the **entire sequence** safely for frontend animation
    """
    env = Environment()
    agent = SimpleAgent(env)
    logs = []
    final_state = []

    while not env.done():
        step_result = agent.step()
        if step_result:
            logs.append(step_result["log"])
            final_state.append(step_result["room"])

    return {"logs": logs, "final_state": final_state}
