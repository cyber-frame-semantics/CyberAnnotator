import streamlit as st
import os
import json
# import nltk
# nltk.download("all")
from nltk.corpus import wordnet as wd
from nltk.corpus import framenet as fn

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

    for m in sub_keys:
        temp = json.dumps(m)
        new_keys = json.loads(temp)

        temp_key = list(new_keys.keys())
        temp_value = list(new_keys.values())

        key_list = key_list + temp_key
        value_list = value_list + temp_value

    st.write(key_list)


    option_of_number = st.multiselect("For which key(s) would you like to go to?",list(range(len(key_list))))
    for i in option_of_number:
        st.write("You selected key: ",i,".",key_list[i])
        st.write(key_list[i],"=",value_list[i])

        hyp_list = []
        syn = wd.synsets(key_list[i])
        for k in syn:
            temp_syn = k.hypernyms()
            for j in temp_syn:
                for p in j.lemmas():
                    hyp_list.append(p.name())

        st.write("Hypernyms of ",key_list[i]," are: ",hyp_list)

        lu_choice_number = st.multiselect("For which hypernyms would you like to see its lexical unit?",list(range(len(hyp_list))),key=i)
        for q in lu_choice_number:
            st.write("You selected hypernyms: ",q,".",hyp_list[q])
            st.write("LUs: ")
            lu = fn.lus(r'%s' %hyp_list[q])
            st.text(lu)

    example.close()
except FileNotFoundError:
    st.error('File not found.')
