from settings import OWM_KEY
import pyowm
from datetime import datetime
import pandas as pd

degree_sign = u'\N{DEGREE SIGN}'
owm = pyowm.OWM(OWM_KEY)
mgr = owm.weather_manager()
obs = mgr.weather_at_place('San Francisco, US')


weather = obs.weather
f_temp = str(int(weather.temperature('fahrenheit')['temp']))

# def get_weathermood():
print(weather)
print('...')
print(f'Your local weather is {weather.detailed_status} with a temperature of')
print(f'{f_temp}{degree_sign}F')
mood = input('How does that make you feel? ')
print(f'When the weather is {weather.detailed_status} and {f_temp}{degree_sign}F, you feel {mood}.')

current_date = [datetime.date(datetime.now()).month, datetime.date(datetime.now()).day, datetime.date(datetime.now()).year ]
current_weather = [weather.detailed_status, f_temp]
weather_mood_date = [current_weather, mood, current_date]
print('...')
print(list(weather_mood_date))
    # return weather_mood_date

# use pandas to create dataframe
df = pd.DataFrame(weather_mood_date)

def weather_today():
    weather_string = "Today's weather is " + weather.detailed_status
    temperature_string = (f"with a temperature of {f_temp}{degree_sign}F")
    return weather_string + " " + temperature_string

def parse_date():
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May',
              6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October',
              11: 'November', 12: 'December'}
    word_month = months[current_date[0]]
    parsed_date = (f'{word_month} {current_date[1]}, {current_date[2]}')
    return parsed_date

# use pandas to create csv`
df.to_csv('weather_mood.csv', index=False)
