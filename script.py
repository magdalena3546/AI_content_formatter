from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key = os.getenv("OPENAI_KEY")
)

with open("article.txt", "r", encoding='utf-8') as file:
    content = file.read()

prompt = '''Przekształć poniższy tekst w kod HTML z odpowiednią strukturą, zawierającą nagłówki, paragrafy oraz miejsca na obrazy. Użyj <img src="image_placeholder.jpg" alt="opis obrazka"> do oznaczenia miejsc na obrazki. Każdy obrazek powinien mieć opis w atrybucie alt oraz podpis pod obrazkiem w tagu <figcaption>. 

Proszę, aby zwrócony kod HTML zawierał tylko treść, która powinna znaleźć się w obrębie tagu <body>. Nie dodawaj tagów <html>, <head> ani <body>.'''

message = f'{prompt} Oto treść artykułu:\n\n{content}'


response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": message
        }
    ],
    max_tokens=1500,
    temperature=0.3
)

with open('artykul.html', 'w', encoding='utf-8') as file:
    file.write(response.choices[0].message.content)