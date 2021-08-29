import streamlit as st
import numpy as np
import pandas as pd

st.write('Let me know about you more.')
## Radio Botton
st.subheader('Which fruit do you like?')
fruit = st.radio(
    'Please select one',
    ('Kiwi', 'Peach', 'Durian','Other'))
st.write('You selected ',fruit)
## Dropdown（select box）
st.subheader('How is your day?')
mind = st.selectbox(
    'Please select one',
    ('Fantastic!!', 'Need Energy!', 'so so','no comment'))
st.write('You selected:', mind)
## multiselect
st.subheader('How do you spend your day?')
way = st.multiselect(
    'Please select',
    ['Youtube', 'Hangout', 'Other'],
    [])
st.write('You selected:', way)