import os
from dotenv import load_dotenv, dotenv_values
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(prompt):
    response = openai.Completion.create(
        engine='gpt-3.5-turbo-instruct',
        prompt=prompt,
        max_tokens=1000,
        temperature=0.7  )

    return response.choices[0].text.strip()
    # return story