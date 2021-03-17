import streamlit as st
import os
import json
import requests
import nltk
#nltk.download()  
from nltk.corpus import wordnet 

filename = st.text_input('Enter a file path:')

try:
    example = open(filename)
    example_read = json.load(example)
    key_list = list(example_read.keys())
    value_list = list(example_read.values())

    sub_keys = []
    for i in value_list:
        if type(i) == list:
            if "{" in str(i[0]):
                sub_keys = sub_keys + i
    st.write(sub_keys)
    for m in sub_keys:
        temp = json.dumps(m)
        new_keys = json.loads(temp)
        temp_list = list(new_keys.keys())
        key_list = key_list + list(set(temp_list) - set(key_list))
    options = st.multiselect('What keys do you want to search', key_list)
    
    
    option_of_number = st.multiselect("for which object would you like to go to?",list(range(len(sub_keys))))
    for i in option_of_number:
        x = sub_keys[i]
        for j in options:
            try:
                st.write(j,"=",x[j])
            except KeyError:
                st.write("That attribute",j,"for",i, "does not exist")

        
    st.write('You selected: ', options)

   # My_sysn = wordnet.synsets("fight") 
    #print("Print just the word:", My_sysn[0].lemmas()[0].name(),"\n")

    example.close()
except FileNotFoundError:
    st.error('File not found.')
