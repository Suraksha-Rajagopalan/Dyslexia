import random
import pandas as pd
import speech_recognition as sr
import pyttsx3
import time

def get_10_word_array(level: int):
    if (level == 1):
        voc = pd.read_csv("intermediate_voc.csv")
        arr = voc.squeeze().to_numpy()
        selected_list = random.sample(list(arr), 10)
        return selected_list
    elif(level == 2):
        voc = pd.read_csv("elementary_voc.csv")
        # return (type(voc))
        arr = voc.squeeze().to_numpy()
        selected_list = random.sample(list(arr), 10) 
        return selected_list
    else:
        return ([])
    
def listen_for(seconds: int):
    with sr.Microphone() as source:
        r = sr.Recognizer()
        audio_data = r.record(source, seconds)
        print("Recognizing...")
        text = r.recognize_google(audio_data)
        print(text)
        return text
    
def talk(Word : str):
    engine = pyttsx3.init()
    engine.say(Word)
    engine.runAndWait()
    
# for i in get_10_word_array():
    
arr = get_10_word_array(2)
print(arr)

rec = []
for i in arr:
    print("repeat: "+i)
    try:
        rec.append(listen_for(3))
    except:
        rec.append("none")
    print("done")
    time.sleep(3)
    
print(rec)   

# listen_for(2.5)