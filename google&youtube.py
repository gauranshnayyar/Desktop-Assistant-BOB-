# Opening and Searching Google and YouTube

import webbrowser 
query = takeCommand().lower()
print(query)
if 'open youtube' in query:
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
       # kat = takeCommand().lower()
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