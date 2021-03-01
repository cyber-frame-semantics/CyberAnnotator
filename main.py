import streamlit as st
import os
import json

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
        temp_list = list(new_keys.keys())
        key_list = key_list + list(set(temp_list) - set(key_list))

    options = st.multiselect('What keys do you want to search', key_list)
    st.write('You selected: ', options)
    example.close()
except FileNotFoundError:
    st.error('File not found.')
