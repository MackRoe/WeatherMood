from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient()
db = client.WeatherMood
weathermoods = db.weathermoods

''' #TODO/DOING: set up an endpoint to deliver collected
weather/mood data'''


@app.route('/')
def index():
    """Return homepage."""
    return render_template('home.html', msg='Weather/Mood is Cool!!')

@app.route('/weather_moods')
def weathermood_index():
    return render_template('weathermood_index.html', weathermoods=weathermoods)




if __name__ == '__main__':
    app.run(debug=True)
