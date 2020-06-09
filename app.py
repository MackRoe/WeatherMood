from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from datetime import datetime
from main import weather_today, parse_date
import os


host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Playlister')
client = MongoClient(host=f'{host}?retryWrites=false')

db = client.WeatherMood
weather = db.weather
moods = db.moods

app = Flask(__name__)

''' #TODO/DOING: set up an endpoint to deliver collected
weather/mood data'''


@app.route('/')
def index():
    """Return homepage test page"""
    return render_template('home.html', msg='Weather/Mood is Cool!!')

@app.route('/moodslist')
def moodslist():
    '''Show recorded moods'''
    return render_template('weathermood_index.html', moods=moods.find())

@app.route('/mood', methods=['POST'])
def wm_submit():
    '''submit a new mood'''
    # get the mood ID
    mood_ids = request.form.get('mood_ids')
    mood = {
        'mood': request.form.get('mood')
    }
    moods.insert_one(mood)
    # return render_template('weathermood_index.html', moods=moods.find())
    return redirect(url_for('index'))

@app.route('/new_mood')
def new_mood():
    """Add a new mood entry"""
    mood = {
        'mood': request.form.get('mood'),
        'weather': request.form.get('weather'),
        'created_at': datetime.now()
    }
    print(mood)
    mood_id = moods.insert_one(mood).inserted_id
    # print(request.form.to_dict())
    return render_template('new_mood.html')

@app.route('/weather_today')
def view_weather_today():
    '''Display today's weather'''
    weather = weather_today()
    date = parse_date()
    return render_template('weather_today.html', weather=weather, date=date)

if __name__ == '__main__':
    app.run(debug=True)
