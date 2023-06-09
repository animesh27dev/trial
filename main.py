from typing import Optional
from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests

app = FastAPI()


@app.get("/url/{url}")
async def root(url: str):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.prettify())
    text = soup.get_text()
    return text


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
