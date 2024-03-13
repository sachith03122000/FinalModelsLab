# tasks.py
import time

from celery import Celery, shared_task
import requests

API_TOKEN = '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'
headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/gpt2"


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


# Initialize Celery
app = Celery('text_generation', broker='redis://localhost/0', backend='redis://localhost/0')

@shared_task
def generate_text(prompt):
    generated_text = query({"inputs": prompt})
    # time.sleep(5)
    return generated_text
