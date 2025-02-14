from fastapi import FastAPI, Path
import requests
import json
from dotenv import load_dotenv
import os
app = FastAPI()

load_dotenv()
API_PROXY_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjIwMDQzOTVAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.TdRiZYPktybtTHafND4s1ketsvQkFPyZ0LH36QezrVI"

@app.post("/run")
async def post_run(task : str):
    url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_PROXY_TOKEN}",
    }
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            { "role": "system", "content": "You are a helpful math tutor. Guide the user through the solution step by step." },
            { "role": "user", "content": "how can I solve 8x + 7 = -23" }
        ]
    }
    response = requests.post(url, headers=headers, json=payload)
    print(response.json())
    return response.json()