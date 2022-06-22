# Min Loop

import pyttsx3
from datetime import date, datetime
from weatherbit.api import Api
import speech_recognition as sr
import wikipedia
import webbrowser 
import random
import requests

code = True
# Assign the voice to the engine
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[0].id)

# Creating a speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Installing an API for weather 
api_key = "5a9939897fed437e82042a2170dc3f37"
api = Api(api_key)
api.set_granularity('daily')
forecast = api.get_forecast(city="Moncton", state="New Brunswick", country="CA")
temprature = forecast.get_series(['temp','precip'])
l = [[x for x in temp.items()] for temp in temprature] 
pal = l[0][0]
t_temp = pal[1]
bro = l[1][0]
tom_temp = bro[1]

# Creating a wish me function
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


# Creating a function to convert user speach to text
def takeCommand():
    import speech_recognition as sr
    r = sr.Recognizer()
    mic = sr.Microphone()
    '''for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))'''
    mic = sr.Microphone(device_index=2)
    with mic as source:
        audio = r.listen(source)
    print('Recognising...')
    quary = r.recognize_google(audio,language = 'en-in')
    return quary

def We_ge(city_name):

    import requests, json
    api_key = "bcf9321b165641d27cb49ad1fca2335d"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    #city_name = input("Enter city name : ")
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name +"&units=" + 'metric'
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
    
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        gau = " Temperature = " +str(current_temperature) +"\n atmospheric pressure = " +str(current_pressure) +"\n humidity = " +str(current_humidity) +"\n description = " +str(weather_description)
        label_g.config(text= gau)
        return gau
    else:
        print(" City Not Found ")

def date_1():
    e = datetime.now().strftime("%Y-%m-%d")
    label_d.config(text=e)
    return e

def time():
    st = datetime.now().strftime("%H:%M:%S")
    label_t.config(text=st)
    return st


def start():
    if __name__ == "__main__":
        wish()
        code = True
        while code:
            speak('how can I help you Master')
            query = takeCommand().lower() #Converting user query into lower case
            print(query)
            # Wikipedia
            if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2) 
                speak("According to Wikipedia")
                print(results)
                speak(results)
        #
            elif 'open youtube' in query:
                speak('Master, do you want to search something perticular on Youtube')
                #webbrowser.open("youtube.com")
                kit = takeCommand().lower()
                print(kit)
                if 'yes' in kit:
                    #url2 = "youtube.com"
                    speak('What would like to search master')
                    kat = takeCommand().lower()
                    if 'play' in kat:
                        web = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                        webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(web))
                        webbrowser.get("chrome").open_new('https://www.youtube.com/watch?v=dx4Teh-nv3A')
                    else:
                        # speak('What would like to search master')
                        #kat = takeCommand().lower()
                        web = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                        webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(web))
                        webbrowser.get("chrome").open_new('https://www.youtube.com/results?search_query=' + kat)
                        #webbrowser.get("chrome").open_new('https://www.youtube.com/watch?v=dx4Teh-nv3A')'''
                elif 'no' in kit:
                    speak('Opening Youtube')
                    #webbrowser.get()
                    url1 = "youtube.com"
                    web = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                    webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(web))
                    webbrowser.get("chrome").open_new(url1)
                #webbrowser.open_new_tab(url1)
            elif 'open google' in query:
                speak('Master, do you want to search something perticular on Google')
                #webbrowser.open("youtube.com")
                kot = takeCommand().lower()
                print(kot)
                if 'yes' in kot:
                    #url2 = "youtube.com"
                    speak('What would like to search master')
                    kqt = takeCommand().lower()
                    web = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                    webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(web))
                    webbrowser.get("chrome").open_new('https://www.google.ca/search?q=' + kqt)
                    #webbrowser.get("chrome").open_new('https://www.youtube.com/watch?v=dx4Teh-nv3A')'''
                elif 'no' in kot:
                    speak('Opening Google')
                    #webbrowser.get()
                    url2 = "google.com"
                    web = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
                    webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(web))
                    webbrowser.get("chrome").open_new(url2)
                    #webbrowser.open_new_tab(url1)
            elif 'play music' in query:
                music_dir = 'C:\Music_Gauransh'
                songs = os.listdir(music_dir)
                random.shuffle(songs)
                speak('Playing Music')
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))
            elif 'time' in query:
                strTime = datetime.now().strftime("%H:%M:%S")
                #current_time = now.strftime("%H:%M:%S")
                print(strTime)
                speak("Master, the time is {}".format(strTime))
            elif 'close' in query:
                speak('Closing the systems')
                puupe = print('Thank you see you next time')
                code = False 

import tkinter as tk
root = tk.Tk()
Height = 600
Width = 800
bg = tk.PhotoImage(file = "SeekPng.com_minions-png_176959.png")
label1 = tk.Label(root, image = bg)
label1.place(x = 0, y = 0)
canvas = tk.Canvas(root, heigh = Height, width= Width)
canvas.pack()
frame = tk.Frame(root, bg = '#80c1ff')
frame.place(relx = 0.05,rely = 0.05, relwidth=0.8, relheight=0.06)
button_t = tk.Button(frame, text= 'TIME', command = lambda: time())
button_t.place(relx= 0.005, rely=0.06, relwidth=0.1, relheight=0.88)
label_t = tk.Label(frame, font = 40, text = '--/--/--')
label_t.place(relx= 0.2, rely=0.06, relwidth=0.797, relheight=0.88)
frame_1 = tk.Frame(root, bg = 'yellow')
frame_1.place(relx = 0.05,rely = 0.15, relwidth=0.8, relheight=0.06)
button_d = tk.Button(frame_1, text= 'Date',command = lambda: date_1())
button_d.place(relx= 0.005, rely=0.06, relwidth=0.1, relheight=0.88)
label_d = tk.Label(frame_1, font = 40, text = '--/--/--')
label_d.place(relx= 0.2, rely=0.06, relwidth=0.797, relheight=0.88)
frame_2 = tk.Frame(root, bg = 'pink')
frame_2.place(relx = 0.05,rely = 0.25, relwidth=0.8, relheight=0.06)
button_w = tk.Button(frame_2, text= 'Weather', command= lambda: We_ge(entry.get()))
button_w.place(relx= 0.005, rely=0.06, relwidth=0.1, relheight=0.88)
entry = tk.Entry(frame_2, font = 40)
entry.place(relx= 0.2, rely=0.06, relwidth=0.797, relheight=0.88)
frame_3 = tk.Frame(root, bg = 'green')
frame_3.place(relx = 0.05,rely = 0.35, relwidth=0.8, relheight=0.45)
label_w = tk.Label(frame_3, font = 40, text = 'Hi I am Bob. I can help you with\t\t\n1) Opening and Searching on Google\n  2) Opening and Searching on Youtube\n\t    3)Playing Muic\t\t\t\t\n    4)Searching Wikipedia\t\t\n    5)Telling time at your place\t\t\n    6)Searcing Weathe\t\t\n To close me you can just say [Close Bob]')
label_w.place(relx= 0.05, rely=0.1, relwidth=0.45, relheight=0.8)
label_g = tk.Label(frame_3, font = 40)
label_g.place(relx= 0.53, rely=0.1, relwidth=0.45, relheight=0.8)
frame_4 = tk.Frame(root, bg = 'black')
frame_4.place(relx = 0.05,rely = 0.85, relwidth=0.8, relheight=0.09)
button_1 = tk.Button(frame_4, text = 'Start', font= 40, command= lambda: start())
button_1.place(relx = 0.05,rely = 0.25, relwidth=0.15, relheight=0.45)
root.mainloop()