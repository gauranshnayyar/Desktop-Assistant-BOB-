# Searching Wikipedia

import wikipedia
if __name__ == "__main__":
    #wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

# Playing Music

query = takeCommand().lower()
import random
if 'play music' in query:
    music_dir = 'C:\Music_Gauransh'
    songs = os.listdir(music_dir)
    random.shuffle(songs)
    speak('Playing Music')
    print(songs)    
    os.startfile(os.path.join(music_dir, songs[0]))

# Speaking Time

import datetime
query = takeCommand().lower()
if 'the time' in query:
    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
    speak("Master, the time is {}".format(strTime))