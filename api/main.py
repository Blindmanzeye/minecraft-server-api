from fastapi import FastAPI
from mcrcon import MCRcon
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

RCON_HOST = os.getenv("RCON_HOST")
RCON_PASSWORD = os.getenv("RCON_PASSWORD")
RCON_PORT = int(os.getenv("RCON_PORT", 25575))

@app.get("/stop-chunky")
def stop_chunky():
    with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
        response = mcr.command("/chunky pause")
    return {"message": "chunky stopped", "response": response}

@app.get("/start-chunky")
def start_chunky():
    with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
        response = mcr.command("/chunky resume")
    return {"message": "chunky started", "response": response}

@app.get("/restart-server")
def restart_server():
    with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
        response = mcr.command("/stop")
    return {"message": "Server restarted", "response": response}
