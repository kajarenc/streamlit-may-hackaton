import streamlit as st
from PIL import Image
import random


st.title("Hello my friend")

if "round" not in st.session_state:
    st.session_state["round"] = {}
if "attempts" not in st.session_state:
    st.session_state["attempts"] = 9

if st.session_state["attempts"] == 0:
    st.balloons()
else:
    img, img_id, actual_result, ai_result = Image.open('3.jpg'), str(random.randint(0, 100))+'3.jpg', 0, 6
    st.image(img, width=600)

    with st.form(key='solution_form', clear_on_submit=True):
        x = st.number_input("Pick a number", min_value=0, max_value=9)
        finished = st.form_submit_button('Submit')

    if finished:
        st.session_state["round"][img_id] = {
            'user_result': x,
            'actual_result': actual_result,
            'ai_result': ai_result
        }
        st.session_state["attempts"] -= 1

    st.write(st.session_state["attempts"])
    st.write(st.session_state["round"])



