from settings import OWM_KEY
import pyowm

degree_sign = u'\N{DEGREE SIGN}'
owm = pyowm.OWM(OWM_KEY)
mgr = owm.weather_manager()
obs = mgr.weather_at_place('San Francisco, US')


weather = obs.weather
f_temp = int(weather.temperature('fahrenheit')['temp'])

print(weather)
print('...')
print(f'Your local weather is {weather.detailed_status} with a temperature of {f_temp}{degree_sign}F')
mood = input('How does that make you feel? ')
print(f'When the weather is {weather.detailed_status} and {f_temp}{degree_sign}F, you feel {mood}.')
