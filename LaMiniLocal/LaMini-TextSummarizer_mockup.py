#! /usr/bin/env python

import streamlit as st
############# Displaying images on the front end #################
st.set_page_config(page_title="Mockup for single page webapp",
                   page_icon='💻',
                   layout="centered",  #or wide
                   initial_sidebar_state="expanded",
                   menu_items={
                        'Get Help': 'https://docs.streamlit.io/library/api-reference',
                        'Report a bug': "https://www.extremelycoolapp.com/bug",
                        'About': "# This is a header. This is an *extremely* cool app!"}
)

# Load image placeholder from the web
st.image('https://placehold.co/750x150', width=750)

# Set a Descriptive Title
st.title("Your Beautiful App Name")
st.divider()
your_future_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras rhoncus massa sit amet est congue dapibus. Duis dictum ac nulla sit amet sollicitudin. In non metus ac neque vehicula egestas. Vestibulum quis justo id enim vestibulum venenatis. Cras gravida ex vitae dignissim suscipit. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Duis efficitur, lorem ut fringilla commodo, lacus orci lobortis turpis, sit amet consequat ante diam ut libero."
st.text_area('Summarized text', your_future_text,
             height = 150, key = 'result')

# Set 2 colums to make the Buttons wider
col1, col2 = st.columns(2)
btn1 = col1.button(" :star: Click ME ", use_container_width=True, type="secondary")
btn2 = col2.button(" :smile: Click ME ", use_container_width=True, type="primary")

if btn1:
    st.warning('You pressed the wrong one!', icon="⚠️")
if btn2:
    st.success('Good Choice!', icon="⚠️")  
st.divider()

