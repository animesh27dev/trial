from typing import Optional
from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests

app = FastAPI()


@app.get("/")
async def root():
    url = request.args.get('url')
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.prettify())
    text = soup.get_text()
    return text
