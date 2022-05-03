from unicodedata import category
from flask import render_template
from app.main import app
from ..request import get_news

@app.route('/')
def home():
    title = 'Debunk News'
    data = "Welcome to Debunk News"
    news=get_news(id)
    return render_template('index.html', title=title, datum=data, articles=news)

