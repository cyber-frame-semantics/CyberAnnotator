import streamlit as st
import os
import json
# import nltk
# nltk.download("all")
from nltk.corpus import wordnet as wd
from nltk.corpus import framenet as fn
from pprint import pprint
from pathlib import Path


# Cache this result, although we probably don't need to
@st.cache
def open_file(filename):
    with open(filename, 'r') as f:
        doc = json.load(f)
        return doc

filename = st.sidebar.file_uploader('Select a file', type=['json'])

# If we haven't selected a file via the above file picker widget, default to this one
if not filename:
    filename = Path('./stix.json')


try:
    example = open_file(filename)

    key_list = list(example.keys())
    value_list = list(example.values())

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

    #Shortcircuit Option 
    shortcircuit_option = st.checkbox("For a given key would you like to see its lexical unit? (shortcircuit to FrameNet option)")
    if shortcircuit_option == True:
        option_of_number = st.multiselect("For which key(s) would you like to see its lexical unit?",list(range(len(key_list))))
        for q in option_of_number:
            st.write("You selected key: ",q,".",key_list[q])
            lu = fn.lus(r'%s' %key_list[q])
            lu_list = [] #List for contructing the string
            lu_nameID_dict = {} #Dictionary for mapping LU_ID w/ LU Name (TODO: Replace the list w/ this dictionary for efficiency)
            for lexical_unit in lu:
                lexical_unit_LU_Name = lexical_unit['name']
                lexical_unit_LU_ID = lexical_unit['ID']
                lu_nameID_dict[lexical_unit_LU_ID] = lexical_unit_LU_Name
                input_str = "LU Name=" + str(lexical_unit_LU_Name) + " (LU ID=" + str(lexical_unit_LU_ID) + ")"
                lu_list.append(input_str)
            if len(lu_list) == 0:
                st.write("No Lexical Units for the selected key")
            else:
                st.write("LUs: ")
                st.write(lu_list)
                LU_choice_number = st.multiselect("For which LU would you like to see it's associated frame and frame elements?",list(range(len(lu_nameID_dict.keys()))),key=i)
                for LU in LU_choice_number:
                    selectedLU = lu_list[LU]
                    if selectedLU.split()[3][0:2] == "ID": #To account for more than one word LU
                        lu_ID = int(selectedLU.split()[3][:-1].replace("ID=", ""))
                    else:
                        lu_ID = int(selectedLU.split()[4][:-1].replace("ID=", ""))
                    lu_name = lu_nameID_dict[lu_ID]
                    st.write("You selected LU: ",LU,".",lu_name)
                    associatedFrame = fn.lu(lu_ID).frame.name
                    lu_frame = fn.frame(associatedFrame)
                    st.write("Frame: ", associatedFrame)
                    st.write("Reference: ",lu_frame.URL)
                    FE_list = []
                    for element in lu_frame.FE:
                        FE_list.append(element)
                    st.write("Frame Elemenet(s): ")
                    st.write(FE_list)
                    st.write("Annotator Summary:")
                    st.write("File Annotated:" , filename)
                    st.write("Selected Key:", key_list[i])
                    st.write("Selected LU:", lu_name)
                    st.write("LU's Frame:", associatedFrame,"(", lu_frame.URL , ")")

    else:
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
                lu = fn.lus(r'%s' %hyp_list[q])
                lu_list = [] #List for contructing the string
                lu_nameID_dict = {} #Dictionary for mapping LU_ID w/ LU Name (TODO: Replace the list w/ this dictionary for efficiency)
                for lexical_unit in lu:
                    lexical_unit_LU_Name = lexical_unit['name']
                    lexical_unit_LU_ID = lexical_unit['ID']
                    lu_nameID_dict[lexical_unit_LU_ID] = lexical_unit_LU_Name
                    input_str = "LU Name=" + str(lexical_unit_LU_Name) + " (LU ID=" + str(lexical_unit_LU_ID) + ")"
                    lu_list.append(input_str)
                if len(lu_list) == 0:
                    st.write("No Lexical Units for the selected hypernym")
                else:
                    st.write("LUs: ")
                    st.write(lu_list)
                    LU_choice_number = st.multiselect("For which LU would you like to see it's associated frame and frame elements?",list(range(len(lu_nameID_dict.keys()))),key=i)
                    for LU in LU_choice_number:
                        selectedLU = lu_list[LU]
                        if selectedLU.split()[3][0:2] == "ID": #To account for more than one word LU
                            lu_ID = int(selectedLU.split()[3][:-1].replace("ID=", ""))
                        else:
                            lu_ID = int(selectedLU.split()[4][:-1].replace("ID=", ""))
                        lu_name = lu_nameID_dict[lu_ID]
                        st.write("You selected LU: ",LU,".",lu_name)
                        associatedFrame = fn.lu(lu_ID).frame.name
                        lu_frame = fn.frame(associatedFrame)
                        st.write("Frame: ", associatedFrame)
                        st.write("Reference: ",lu_frame.URL)
                        FE_list = []
                        for element in lu_frame.FE:
                            FE_list.append(element)
                        st.write("Frame Elemenet(s): ")
                        st.write(FE_list)
                        st.write("Annotator Summary:")
                        st.write("File Annotated:" , filename)
                        st.write("Selected Key:", key_list[i])
                        st.write("Selected Hypernym:", hyp_list[q])
                        st.write("Selected LU:", lu_name)
                        st.write("LU's Frame:", associatedFrame,"(", lu_frame.URL , ")")
                        
except FileNotFoundError:
    st.error('File not found.')
