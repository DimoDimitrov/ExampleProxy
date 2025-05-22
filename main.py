from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import requests
from requests.exceptions import RequestException
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = FastAPI()

@app.get("/proxy/session")
def get_session_id():
    auth_token = os.getenv("AUTH_TOKEN")
    if not auth_token:
        raise HTTPException(status_code=500, detail="AUTH_TOKEN not configured")

    try:
        response = requests.get(
            "https://sportensklad.bg/index.php?route=aiapi/cart/sess",
            headers={
                "Authorization": f"Bearer {auth_token}",
                "Cache-Control": "no-cache",
                "User-Agent": "PostmanRuntime/7.44.0",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }
        )
        response.raise_for_status()  # Raise an exception for bad status codes
        session_id = response.text.strip()
        return JSONResponse(content={"sessionID": session_id})
    except RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch session ID: {str(e)}")
