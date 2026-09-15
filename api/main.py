from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from mcrcon import MCRcon
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()
security = HTTPBearer()

RCON_HOST = os.getenv("RCON_HOST")
RCON_PASSWORD = os.getenv("RCON_PASSWORD")
RCON_PORT = int(os.getenv("RCON_PORT", 25575))

@app.get("/stop-chunky")
def stop_chunky(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    if token != os.getenv("SERVER_SECRET_KEY"):
        raise HTTPException(status_code=401, detail="Invalid token")
    with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
        response = mcr.command("/chunky pause")
    return {"message": "chunky stopped", "response": response}

@app.get("/start-chunky")
def start_chunky(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    if token != os.getenv("SERVER_SECRET_KEY"):
            raise HTTPException(status_code=401, detail="Invalid token")
    with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
        response = mcr.command("/chunky resume")
    return {"message": "chunky started", "response": response}

@app.get("/restart-server")
def restart_server(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    if token != os.getenv("SERVER_SECRET_KEY"):
            raise HTTPException(status_code=401, detail="Invalid token")
    with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
        response = mcr.command("/stop")
    return {"message": "Server restarted", "response": response}

@app.get("/start-server")
def start_server(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    if token != os.getenv("SERVER_SECRET_KEY"):
            raise HTTPException(status_code=401, detail="Invalid token")
    bash_path = os.getenv("BASH_PATH")
    if not bash_path:
        return {"error": "BASH_PATH is not set in the environment variables."}
    os.system(f"bash {bash_path}/start.sh")