from flask import render_template
from app import app

@app.route('/')
def home():
    title = 'Debunk News'
    data = "Welcome to Debunk News"
    return render_template('index.html', datum=data, title=title)

