from flask import Blueprint, render_template, request
from app.sentiment_model import analyze_sentiment

routes = Blueprint('routes', __name__)

@routes.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        user_input = request.form['text']
        result = analyze_sentiment(user_input)
    return render_template('index.html', result=result)
