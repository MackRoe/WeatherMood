from settings import OWM_KEY
import pyowm

degree_sign = u'\N{DEGREE SIGN}'
owm = pyowm.OWM(OWM_KEY)
mgr = owm.weather_manager()
obs = mgr.weather_at_place('San Francisco, US')


weather = obs.weather
f_temp = weather.temperature('fahrenheit')['temp']

print(weather)
print('...')
print(f'Your local weather is {weather.status} with a temperature of {f_temp}{degree_sign}F')
