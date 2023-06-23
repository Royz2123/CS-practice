import glob
import os
from typing import Callable, Dict

import streamlit as st

from common.utils import display_name
from components.body_rtl import set_body_rtl
from webpages.exercise_page import write_exercise_page
from webpages.home_page import write_home_page
from webpages.about_page import write_about_page

EXERCISES_BASE_DIR_PATH = "exercises"


def get_all_exercise_pages() -> Dict[str, Callable]:
    exercise_pages = {}
    for chapter_dir_name in os.listdir(EXERCISES_BASE_DIR_PATH):
        if not chapter_dir_name.startswith("Chapter"):
            continue

        chapter_dir_path = os.path.join(EXERCISES_BASE_DIR_PATH, chapter_dir_name)
        for exercise_dir_name in os.listdir(chapter_dir_path):
            if not exercise_dir_name.startswith("Exercise"):
                continue

            exercise_dir_path = os.path.join(chapter_dir_path, exercise_dir_name)
            exercise_pages[display_name(exercise_dir_name)] = lambda x=exercise_dir_path: write_exercise_page(x)
    return exercise_pages


def test_page():
    all_pages = get_all_exercise_pages()
    with st.sidebar.expander("See explanation"):
        for page_name, page_action in all_pages.items():
            st.sidebar.button(page_name, on_click=page_action)


PAGES = {
    "🏠 עמוד הבית": write_home_page,
    "🏠 מידע נוסף": write_about_page,
    "✏️ תרגילים": write_exercise_page,
    **get_all_exercise_pages()
}

st.set_page_config(
    page_title='יסודות מדעי המחשב',
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
set_body_rtl()

selected_page_name = st.sidebar.radio(
    "Select Page",
    PAGES.keys(),
    label_visibility="collapsed"
)


def display_page(page_name: str) -> None:
    st.title(page_name)
    PAGES[page_name]()


display_page(selected_page_name)


