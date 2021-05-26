import streamlit as st
from PIL import Image
import random

st.title("AAA")

if "rounds_info" not in st.session_state:
    st.session_state["rounds_info"] = {}

if "current_round" not in st.session_state:
    st.session_state["current_round"] = 1

if "current_photo_name" not in st.session_state:
    st.session_state["current_photo_name"] = 0


def callback():
    st.session_state["rounds_info"][img_id] = {
        'actual_result': actual_result,
        'ai_result': ai_result,
        'user_result': x
    }

    st.session_state["current_round"] += 1
    st.session_state["current_photo_name"] += 1


if st.session_state["current_round"] < 10:
    img_name = str(st.session_state["current_photo_name"]) + '.png'
    img, img_id, actual_result, ai_result = Image.open(img_name), str(random.randint(0, 100)) + "_" + img_name, 77, 6
    st.image(img, width=400)

    x = st.number_input("Pick a number", min_value=0, max_value=9)
    st.button('Submit', on_change=callback)

    st.write(st.session_state["current_round"])
    st.write(st.session_state["current_photo_name"])
    st.write(st.session_state["rounds_info"])
