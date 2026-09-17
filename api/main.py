from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from mcrcon import MCRcon
from dotenv import load_dotenv
import os
import subprocess

load_dotenv()
app = FastAPI()
security = HTTPBearer()

RCON_HOST = os.getenv("RCON_HOST", "localhost")
RCON_PASSWORD = os.getenv("RCON_PASSWORD", "sixseven")
RCON_PORT = int(os.getenv("RCON_PORT", 25575))

@app.get("/stop-chunky")
def stop_chunky(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    if token != os.getenv("SERVER_SECRET_KEY", "sixseven"):
        raise HTTPException(status_code=401, detail="Invalid token")
    def _run():
        with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
            return mcr.command("/chunky pause")
    return _run()

@app.get("/start-chunky")
async def start_chunky(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    if token != os.getenv("SERVER_SECRET_KEY", "sixseven"):
            raise HTTPException(status_code=401, detail="Invalid token")
    def _run():
        with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
            return mcr.command("say this is a test command for something that the owner is working on epstien fuck jews")
    return _run()

@app.get("/restart-server")
async def restart_server(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    if token != os.getenv("SERVER_SECRET_KEY"):
            raise HTTPException(status_code=401, detail="Invalid token")
    def _run():
        with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
            return mcr.command("/stop")
    return _run()

@app.get("/start-server")
async def start_server(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    if token != os.getenv("SERVER_SECRET_KEY"):
            raise HTTPException(status_code=401, detail="Invalid token")
    bash_path = os.getenv("BASH_PATH")
    if not bash_path:
        return {"error": "BASH_PATH is not set in the environment variables."}
    subprocess.run(["bash", f"{bash_path}/start.sh"])
