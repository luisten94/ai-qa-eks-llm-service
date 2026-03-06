from fastapi import FastAPI, HTTPException
import requests
import os

app = FastAPI()

VLLM_ENDPOINT = os.getenv("VLLM_ENDPOINT", "http://vllm-service:8000/generate")

@app.post("/ask")
def ask(question: str):

    try:
        payload = {
            "prompt": question,
            "max_tokens": 100
        }

        response = requests.post(VLLM_ENDPOINT, json=payload)

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="LLM error")

        return {
            "question": question,
            "answer": response.json()
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))