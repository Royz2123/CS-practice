import os
import uuid
from typing import Callable, Dict

import streamlit as st
from streamlit.components.v1 import html

from common.utils import display_name
from components.set_direction import set_direction
from webpages.about_page import write_about_page
from webpages.chapter_page import write_chapter_page
from webpages.exercise_intro_page import write_exercises_intro_page
from webpages.exercise_page import write_exercise_page
from webpages.home_page import write_home_page


# TODO: Style more, change to a single color palette
# TODO: Think about save mode with session state
# TODO: Think about admin mode for playing with exercises, maybe replacing sol and such

def get_all_exercise_pages() -> Dict[str, Callable]:
    exercise_pages = {}
    for chapter_dir_name in os.listdir("exercises"):
        # Handle chapter
        if not chapter_dir_name.startswith("Chapter"):
            continue
        chapter_dir_path = os.path.join("exercises", chapter_dir_name)
        exercise_pages[display_name(chapter_dir_name)] = lambda x=chapter_dir_path: write_chapter_page(x)

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
    "❓ איך מתחילים?": write_about_page,
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
            .css-z5fcl4 {
                padding-top: 1rem;
                padding-bottom: 0rem;
                padding-left: 5rem;
                padding-right: 5rem;
            }
            .st-cf:hover {
                background-color: #bee1e5;
                transition: 0.3s;
                transform: scale(1.05); 
            }
            .st-c2 {
                width: 0rem;
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
    PAGES[page_name]()


display_page(selected_page_name)
html(
    f"""
        <script id={uuid.uuid4()}>
            console.log("Including indentation script");

            function getNavBar() {{
                // let navBarElements = window.parent.document.getElementsByClassName("st-b3 st-bd st-be st-bf st-bg st-bh");
                let navBarElements = window.parent.document.getElementsByTagName("body");
                console.log(navBarElements);
                if (navBarElements.length > 0) {{
                    console.log("Found NavBar!");
                    return navBarElements[0]; 
                }}
                console.log("No navbar not found :(");
                return null; 
            }}

            function setIndentation() {{
                console.log("Setting Indentation");
                // First, make this iframe smaller on the way
                allRadios = window.parent.document.getElementsByClassName("st-c1 st-cf st-cg st-ae st-af st-ag st-ah st-ai st-aj st-ch st-ci");
                console.log(allRadios);
                for (let i = 0; i < allRadios.length; i++) {{
                    if(allRadios[i].innerHTML.startsWith("📄")) {{
                        allRadios[i].innerHTML = "&emsp;&emsp;" + allRadios[i].innerHTML;
                    }}
                    if(allRadios[i].innerHTML.startsWith("📂")) {{
                        allRadios[i].innerHTML = "&emsp;" + allRadios[i].innerHTML;
                    }}
                }}
            }}

            // Set trigger for indentation script
            radioNavBar = getNavBar()
            setIndentation();
            // setTimeout(setIndentation, 1000); 
            // radioNavBar.addEventListener("load", setIndentation);
        </script>
    """
)