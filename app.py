from PIL import Image
import numpy as np
import streamlit as st
from mnist import get_results

st.title("AAA")

if "match_number" not in st.session_state:
    st.session_state["match_number"] = 1


@st.cache()
def get_game_data(game_number):
    return get_results()


def gen_image(arr):
    two_d = (np.reshape(arr, (28, 28)) * 255).astype(np.uint8)
    return Image.fromarray(two_d, "L")


game_data = get_game_data(st.session_state["match_number"])
st.write(game_data)

if "rounds_info" not in st.session_state:
    st.session_state["rounds_info"] = {}

if "current_round" not in st.session_state:
    st.session_state["current_round"] = 0


def new_game():
    st.session_state["match_number"] += 1
    st.session_state["current_round"] = 0


def callback():
    st.session_state["rounds_info"][st.session_state["current_round"]] = {
        "actual_result": actual_result,
        "ai_result": ai_prediction,
        "user_result": x
    }

    st.session_state["current_round"] += 1


if st.session_state["current_round"] < 10:
    current_image = game_data[st.session_state["current_round"]]["image_np"]
    actual_result = game_data[st.session_state["current_round"]]["label"]
    ai_prediction = game_data[st.session_state["current_round"]]["prediction"]

    st.image(gen_image(current_image), width=400)

    x = st.number_input("Pick a number", min_value=0, max_value=9, )
    st.button("Submit", on_change=callback)

    st.write("CURRENT ROUND")
    st.write(st.session_state["current_round"])
    st.write("CURRENT_X")
    st.write(x)

else:

    ai_score = 0
    user_score = 0

    for key, value in st.session_state["rounds_info"].items():

        if value["ai_result"] == value["actual_result"]:
            ai_score += 1

        if value["user_result"] == value["actual_result"]:
            user_score += 1

    if user_score >= ai_score:
        st.balloons()

    st.button("PLAY AGAIN", on_change=new_game)

    st.write(f"YOUR SCORE: {user_score}!")
    st.write(f"AI SCORE: {ai_score}")
