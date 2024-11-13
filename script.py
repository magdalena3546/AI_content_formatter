from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key = os.getenv("OPENAI_KEY")
)

response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Say this is a test"
        }
    ],
    max_tokens=500
)

print(response.choices[0].message.content)