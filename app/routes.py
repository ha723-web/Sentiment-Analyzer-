from flask import Blueprint, render_template, request
from app.sentiment_model import analyze_sentiment

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    if request.method == 'POST':
        text = request.form['text']
        sentiment = analyze_sentiment(text)
    return render_template('index.html', sentiment=sentiment)
