from flask import render_template
from . import main
from ..request import get_news

@main.route('/')
def home():
    title = 'Debunk News'
    data = "Welcome to Debunk News"
    news=get_news()
    return render_template('index.html', title=title, datum=data, articles=news)

