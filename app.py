from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from main import weather_today

app = Flask(__name__)

client = MongoClient()
db = client.WeatherMood
weathermoods = db.weathermoods

''' #TODO/DOING: set up an endpoint to deliver collected
weather/mood data'''


@app.route('/')
def index():
    """Return homepage test page"""
    return render_template('home.html', msg='Weather/Mood is Cool!!')


@app.route('/weather_moods')
# route for list of each day's weather and mood
# change '/weathermoods' to '/' after populating db
def weathermood_index():
    return render_template('weathermood_index.html', weathermoods=weathermoods)


@app.route('/new_mood')
def new_mood():
    """Create a new playlist."""
    return render_template('new_mood.html')

@app.route('/weather_today')
def view_weather_today():
    '''Display today's weather'''
    weather = weather_today()
    return render_template('weather_today.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
