import streamlit as st
import os
import json
# import nltk
# nltk.download("all")
from nltk.corpus import wordnet as wd
from nltk.corpus import framenet as fn
from pprint import pprint

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
            lu = str(fn.lus(r'%s' %hyp_list[q]))
            lu = lu[1:-1]
            lu_list = lu.split(", ")
            st.write(lu_list)
            LU_choice_number = st.multiselect("For which LU would you like to see it's associated frame and frame elements?",list(range(len(lu_list))),key=i)
            #TODO: Fix issue of  LU list's containing ..., as this isn't a valid LU entry
            for LU in LU_choice_number:
                selectedLU = lu_list[LU]
                lu_name = selectedLU.split("=")[2][:-1]
                st.write("You selected LU: ",LU,".",lu_name)
                lu_ID = int(selectedLU.split()[1][3:])
                associatedFrame = fn.lu(lu_ID).frame.name
                lu_frame = fn.frame(associatedFrame)
                st.write("Frame: ", associatedFrame)
                st.write("Reference: ",lu_frame.URL)
                FE_list = []
                for element in lu_frame.FE:
                    FE_list.append(element)
                st.write("Frame Elemenet(s): ")
                st.write(FE_list)
            

    example.close()
except FileNotFoundError:
    st.error('File not found.')
