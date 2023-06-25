import os
from typing import Callable, Dict

import streamlit as st

from common.errors import RecognizedSiteException
from common.utils import display_name, indent_menu
from components.error import write_error
from components.set_direction import set_direction
from webpages.about_page import write_about_page
from webpages.chapter_page import write_chapter_page
from webpages.exercise_intro_page import write_exercises_intro_page
from webpages.exercise_page import write_exercise_page
from webpages.home_page import write_home_page


# TODO: Think about save mode with session state
# TODO: Think about admin mode for playing with exercises, maybe replacing sol and such
# TODO: Improve menu more - selectable options on whole line, smooth transition, smaller width, collapsable button on right

def get_all_exercise_pages() -> Dict[str, Callable]:
    exercise_pages = {}
    for chapter_dir_name in os.listdir("exercises"):
        # Handle chapter
        if not chapter_dir_name.startswith("Chapter"):
            continue
        chapter_dir_path = os.path.join("exercises", chapter_dir_name)
        exercise_pages[display_name(chapter_dir_name)] = lambda x=chapter_dir_name: write_chapter_page(x)

        # Handle exercises under the chapter
        for exercise_dir_name in os.listdir(chapter_dir_path):
            if not exercise_dir_name.startswith("Exercise"):
                continue

            exercise_dir_path = os.path.join(chapter_dir_path, exercise_dir_name)
            exercise_pages[display_name(exercise_dir_name)] = lambda x=exercise_dir_path: write_exercise_page(x)

    # Sort based on display name (without icon)
    exercise_pages = dict(sorted(exercise_pages.items(), key=lambda x: x[0][1:]))
    return exercise_pages


def test_page():
    all_pages = get_all_exercise_pages()
    with st.sidebar.expander("See explanation"):
        for page_name, page_action in all_pages.items():
            st.sidebar.button(page_name, on_click=page_action)


PAGES = {
    "🏠 עמוד הבית": write_home_page,
    "⏯️ איך מתחילים?": write_about_page,
    "✏️ תרגילים": write_exercises_intro_page,
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
set_direction("body")

st.markdown(
    """
        <style>
            h1, h2, h3, p, div {
            	font-family: 'Segoe UI';
            }
        
            .css-z5fcl4 {
                padding-top: 1rem;
                padding-bottom: 0rem;
                padding-left: 5rem;
                padding-right: 5rem;
            }
            #menuRadioOption {
                font-family: 'Segoe UI';
            }
            #menuRadioOption:hover {
                background-color: #bee1e5;
                transition: 0.3s;
                transform: scale(1.05); 
                border-radius: 5px;
            }
            div[data-testid="stExpander"] div[role="button"] p {
                font-size: 1rem;
            }
            img {
                border-style: solid;
            }
        </style>
    """,
    unsafe_allow_html=True
)

selected_page_name = st.sidebar.radio(
    "Select Page",
    PAGES.keys(),
    label_visibility="collapsed",
)


def display_page(page_name: str) -> None:
    st.title(page_name)
    st.divider()
    PAGES[page_name]()


placeholder = st.empty()
try:
    with placeholder.container():
        display_page(selected_page_name)
        indent_menu()
except RecognizedSiteException as e:
    with placeholder.container():
        write_error(str(e))
except Exception as e:
    raise e
    with placeholder.container():
        write_error("האמת שאנחנו לא עד הסוף מבינים מה קרה ... להלן הפירוט:", str(e))
