from fastapi import FastAPI, Path
import requests
import json
from dotenv import load_dotenv
import os
app = FastAPI()

load_dotenv()
API_PROXY_TOKEN = os.getenv("AIPROXY_TOKEN")


@app.post("/run")
async def post_run(task : str):
    url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_PROXY_TOKEN}",
    }
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": "A task would be given to you. Identify if the task is asking to: install uv and run a link. Reply with 'yes' or 'no'."
            },
            {
                "role": "user",
                "content": task
            }
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "interpret_task",
                "strict":True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "steps": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {"explanation": {"type": "string"}, "output": {"type": "string"}},
                                "required": ["explanation", "output"],
                                "additionalProperties": False
                            }
                        },
                        "final_answer": {"type": "string"}
                    },
                    "required": ["steps", "final_answer"],
                    "additionalProperties": False
                }
            }
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    print(response.json())
    return response.json()