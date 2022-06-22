# Making Function to take command

def takeCommand():
    import speech_recognition as sr
    r = sr.Recognizer()
    mic = sr.Microphone()
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
    mic = sr.Microphone(device_index=2)
    with mic as source:
        audio = r.listen(source)
    print('Recognising...')
    quary = r.recognize_google(audio,language = 'en-in')
    return quary
takeCommand()