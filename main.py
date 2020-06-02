from settings import OWM_KEY
import pyowm

owm = pyowm.OWM(OWM_KEY)
mgr = owm.weather_manager()
obs = mgr.weather_at_place('San Francisco, US')

weather = obs.weather
print(weather)
