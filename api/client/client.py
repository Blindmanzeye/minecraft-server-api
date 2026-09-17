import requests
from dotenv import load_dotenv
import getpass
import os

load_dotenv()

SECRET_KEY = getpass.getpass("Enter Secret key: ")
if not SECRET_KEY:
    SECRET_KEY = os.getenv("SECRET_KEY")

SERVER_URL = os.getenv("SERVER_URL", "mc.blindmanzeye.me")
headers = {
    "Authorization": f"Bearer {SECRET_KEY}",
    "Content-type": "application/json"
}

def send_request(endpoint: str):
    url = f"{SERVER_URL}/{endpoint}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

while True:
    print("\nAvailable commands:")
    print("1. Stop Chunky")
    print("2. Start Chunky")
    print("3. Restart Server")
    print("4. Start Server")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        result = send_request("stop-chunky")
        print(result)
    elif choice == "2":
        result = send_request("start-chunky")
        print(result)
    elif choice == "3":
        result = send_request("restart-server")
        print(result)
    elif choice == "4":
        result = send_request("start-server")
        print(result)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")