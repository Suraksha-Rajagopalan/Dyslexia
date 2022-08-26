import streamlit as st
import time
import pandas as pd
import random
import pyttsx3


def talk(Word : str):
    engine = pyttsx3.init()
    engine.say(Word)
    engine.runAndWait()
    
def get_10_word_array(level: int):
    if (level == 1):
        voc = pd.read_csv("intermediate_voc.csv")
        arr = voc.squeeze().to_numpy()
        selected_list = random.sample(list(arr), 10)
        return selected_list
    elif(level == 2):
        voc = pd.read_csv("elementary_voc.csv")
        arr = voc.squeeze().to_numpy()
        selected_list = random.sample(list(arr), 10) 
        return selected_list
    else:
        return ([])
    
def dictate_10_words(level : int):
    words = get_10_word_array(level)
    for i in words:
        talk(i)
        time.sleep(5)
    return words

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


level = 1

option = st.selectbox(
            "select your standard", ('2nd-4th', '5th-7th'), key= "pro")
if option=='2nd-4th':
    level = 2
elif option == '5th-7th':
    level = 1
    
form = st.form(key='my_form')
w1 = form.text_input(label='word1')
w2 = form.text_input(label='word2')
w3 = form.text_input(label='word3')
w4 = form.text_input(label='word4')
w5 = form.text_input(label='word5')
w6 = form.text_input(label='word6')
w7 = form.text_input(label='word7')
w8 = form.text_input(label='word8')
w9 = form.text_input(label='word9')
w10 = form.text_input(label='word10')
submit_button = form.form_submit_button(label='Submit')



@st.cache
def bind_socket():
    # This function will only be run the first time it's called
    dictated_words = dictate_10_words(level)
    return dictated_words
    
    
dictated_words = bind_socket() 
# print(dictated_words)

if submit_button:
    typed_words = []
    typed_words.append(w1)
    typed_words.append(w2)
    typed_words.append(w3)
    typed_words.append(w4)
    typed_words.append(w5)
    typed_words.append(w6)
    typed_words.append(w7)
    typed_words.append(w8)
    typed_words.append(w9)
    typed_words.append(w10)
    
    print(typed_words)
    print(dictated_words)
    
    st.write("your dictation score is (lesser the better) : " , levenshtein(" ".join(typed_words) , " ".join(dictated_words)))
    st.write("dictated words: " + " ".join(dictated_words))
    st.write("typed words: " + " ".join(typed_words))