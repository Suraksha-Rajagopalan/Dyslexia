import random
import pandas as pd
import speech_recognition as sr
import pyttsx3
import time
import eng_to_ipa as ipa
import streamlit as st

#'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

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
    
#'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
    
def listen_for(seconds: int):
    with sr.Microphone() as source:
        r = sr.Recognizer()
        print("Recognizing...")
        audio_data = r.record(source, seconds)
        text = r.recognize_google(audio_data)
        print(text)
        return text
 
 #'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
    
def talk(Word : str):
    engine = pyttsx3.init()
    engine.say(Word)
    engine.runAndWait()
    
#'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
    
def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            # j+1 instead of j since previous_row and current_row are one character longer
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

#'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

def check_pronounciation(str1 : str , str2: str):
    s1 = ipa.convert(str1)
    s2 = ipa.convert(str2)
    return levenshtein(s1,s2)

#'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
    
def dictate_10_words(level : int):
    words = get_10_word_array(level)
    for i in words:
        talk(i)
        time.sleep(8)
    return words

#'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
tab1, tab2, tab3 = st.tabs(["Home", "pronounciation test", "listening test"])

with tab1:
    st.title("A Test for Dyslexia")

with tab2:
    st.header("The pronounciation and reading ability of the user will be measured here")
    pronounciation_test = st.button("Start a pronouncation test")

    pronounciation_inaccuracy = 0
    level = 0
    option = st.selectbox(
            "select your standard", ('2nd-4th', '5th-7th'), key= "pro")
    if option=='2nd-4th':
        level = 2
    elif option == '5th-7th':
        level = 1
           
    if pronounciation_test:
        st.subheader("Please repeate the following words you only has 20 seconds to do that.")
         
        arr = get_10_word_array(level)
        for i in range(len(arr)):
            arr[i] = str(arr[i])
            arr[i] = arr[i].strip()

        str_displayed = str(" ".join(arr))
        words = st.text(">> " + "\n>>".join(arr) )
        status = st.text("listenning........")
        str_pronounced = listen_for(30)
        status.write("Time up! calculating inacuracy......")
        # str_displayed = " ".join(arr)
        pronounciation_inaccuracy = check_pronounciation(str_displayed, str_pronounced)/len(str_displayed)
        words.write("the pronounciation inacuuracy is: " + str(pronounciation_inaccuracy))
    
      
    
with tab3:   
    written_words =[]
    st.header("The listening ability of the user will be measured here")
    dictation_inacuracy = 0
    level = 0
    option = st.selectbox(
            "select your standard", ('2nd-4th', '5th-7th'), key= "read")
    if option=='2nd-4th':
        level = 2
    elif option == '5th-7th':
        level = 1
    
    word_array = get_10_word_array(level)
    
    start = st.button("start the test")
    
    if start:
        talk(word_array[0])
       
    st.write('please type the word you heard below')
    form1 = st.form(key='word1')
    name1 = form1.text_input('word 1')
    submit1 = form1.form_submit_button('Submit')
    if submit1:
        st.write(f'hello {name1}')
        time.sleep(2)
        talk(word_array[1])
        
        

    st.write('please type the word you heard below')
    form2 = st.form(key='word2')
    name2 = form2.text_input('word 2')
    submit2 = form2.form_submit_button('Submit')
    if submit2:
        st.write(f'hello {name2}')
        time.sleep(2)
        talk(word_array[2])
        
        
    st.write('please type the word you heard below')
    form3 = st.form(key='word3')
    name3 = form3.text_input('word 3')
    submit3 = form3.form_submit_button('Submit')
    if submit3:
        st.write(f'hello {name3}')
        time.sleep(2)
        talk(word_array[3])
        
        
    st.write('please type the word you heard below')
    form4 = st.form(key='word4')
    name4 = form4.text_input('word 4')
    submit4 = form4.form_submit_button('Submit')
    if submit4:
        st.write(f'hello {name4}')
        time.sleep(2)
        talk(word_array[4])
        
    st.write('please type the word you heard below')
    form5 = st.form(key='word5')
    name5 = form5.text_input('word 5')
    submit5 = form5.form_submit_button('Submit')
    if submit5:
        st.write(f'hello {name5}')
        time.sleep(2)
        talk(word_array[5])
        
    st.write('please type the word you heard below')
    form6 = st.form(key='word6')
    name6 = form6.text_input('word 6')
    submit6 = form6.form_submit_button('Submit')
    if submit6:
        st.write(f'hello {name6}')
        time.sleep(2)
        talk(word_array[6])
    