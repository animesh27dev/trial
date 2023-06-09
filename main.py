from flask import Flask, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    url = request.args.get('url')
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = soup.get_text()
    return text

if __name__ == '__main__':
    app.run(debug=True)
