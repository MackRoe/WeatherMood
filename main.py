from settings import OWM_KEY
import pyowm
from datetime import datetime

degree_sign = u'\N{DEGREE SIGN}'
owm = pyowm.OWM(OWM_KEY)
mgr = owm.weather_manager()
obs = mgr.weather_at_place('San Francisco, US')


weather = obs.weather
f_temp = int(weather.temperature('fahrenheit')['temp'])

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
