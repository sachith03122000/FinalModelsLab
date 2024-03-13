from transformers import pipeline

# print(data)

# Print generated text
# main.py
from tasks import generate_text

# List of prompts
prompts = ["Once upon a time", "In a galaxy far, far away"]

# Call Celery task for each prompt
for prompt in prompts:
    result = generate_text.delay(prompt)
    for v in result.collect():
        print(v[1])

