# Importing Engine to get detail of the voice and to make a peach fnction

import pyttsx3
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)

# Making Speach function using engine and using a weatherbit API to tell the average temprate of the city you choose

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

from datetime import date, datetime
from weatherbit.api import Api
api_key = "5a9939897fed437e82042a2170dc3f37"
api = Api(api_key)
api.set_granularity('daily')
forecast = api.get_forecast(city="Moncton", state="New Brunswick", country="CA")
temprature = forecast.get_series(['temp','precip'])
print(temprature)
l = [[x for x in temp.items()] for temp in temprature] 
pal = l[0][0]
t_temp = pal[1]
bro = l[1][0]
tom_temp = bro[1]

# Making a Wish Function

def wish():
    today = date.today()
    clock = datetime.now()
    currnt_hr = clock.hour
    if currnt_hr < 12:
        speak('Good morning Master Todays date is')
        speak(today)
        speak('and the average temprature of today is')
        speak(t_temp)
        speak('Celsius')
        speak('And Master Tomorrows average temprature will be')
        speak(tom_temp)
        speak('Celsius')
    elif currnt_hr > 12 and currnt_hr <= 18:
        speak('Good AfterNoon Master Todays date is')
        speak(today)
        speak('and the average temprature of today is')
        speak(t_temp)
        speak('Celsius')
        speak('And Master Tomorrows average temprature will be')
        speak(tom_temp)
        speak('Celsius')
    else:
        speak('Good Night Master Todays date is')
        speak(today)
        speak('and the average temprature of today is')
        speak(t_temp)
        speak('Celsius')
        speak('And Master Tomorrows average temprature will be')
        speak(tom_temp)
        speak('Celsius')