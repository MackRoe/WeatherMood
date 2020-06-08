from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient()
db = client.Playlister
playlists = db.playlists

''' #TODO/DOING: set up an endpoint to deliver collected
weather/mood data'''


@app.route('/weather_mood_list')
def weather_mood_list():
    return
