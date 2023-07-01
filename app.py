import logging
import os
from pprint import pprint
from typing import List

import streamlit as st

from common.exceptions import RecognizedSiteException, InvalidExerciseException, InvalidChapterException, Redirect
from common.utils import indent_menu
from components.error import write_error
from components.set_direction import set_direction
from webpages.about_page import AboutPage
from webpages.base_page import BasePage
from webpages.chapter_page import ChapterPage
from webpages.exercise_intro_page import ExerciseIntoPage
from webpages.exercise_page import ExercisePage
from webpages.home_page import HomePage


# TODO: Think about save mode with session state
# TODO: Think about admin mode for playing with exercises, maybe replacing sol and such
# TODO: Improve menu more - selectable options on whole line, smooth transition, smaller width, collapsable button on right
# TODO: maybe no pdf, just docx and python takes care of the rest
# TODO: display as ints if given as ints
# TODO: Fix menu on load shit

def get_all_dynamic_pages() -> List[BasePage]:
    all_pages = []
    chapter_pages = []
    for chapter_dir_name in os.listdir("exercises"):
        # Don't even attempt to create chapters that are clearly invalid
        chapter_dir_path = os.path.join("exercises", chapter_dir_name)
        if not (os.path.isdir(chapter_dir_path) and ChapterPage.valid_dir_name(chapter_dir_name)):
            continue

        # Handle exercises under the chapter
        chapter_exercise_pages = []
        for exercise_dir_name in os.listdir(chapter_dir_path):
            exercise_dir_path = os.path.join(chapter_dir_path, exercise_dir_name)
            try:
                # Don't even attempt to create exercises that are clearly invalid
                if not (os.path.isdir(exercise_dir_path) and ExercisePage.valid_dir_name(exercise_dir_name)):
                    continue
                chapter_exercise_pages.append(ExercisePage(exercise_dir_name, chapter_dir_name))
            except InvalidExerciseException as e:
                logging.warning(f"Got InvalidExerciseException for {exercise_dir_name}, skipping... {e}")

        # Add chapter page as well
        try:
            chapter_page = ChapterPage(chapter_dir_name, chapter_exercise_pages)
            all_pages.append(chapter_page)
            chapter_pages.append(chapter_page)
            all_pages.extend(chapter_exercise_pages)
        except InvalidChapterException as e:
            logging.warning(f"Got InvalidChapterException for {chapter_dir_name}, skipping... {e}")

    # Add exercise intro page
    all_pages.append(ExerciseIntoPage(chapter_pages))
    return all_pages


# Create sorted list of all pages based on menu index
PAGES: List[BasePage] = [
    HomePage(),
    AboutPage(),
    *get_all_dynamic_pages()
]
PAGES.sort(key=lambda page: page.menu_index)
pprint(PAGES)

# Set general app stuff
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
            h1, h2, h3, p, div, ul, li {
            	font-family: 'Segoe UI';
            }
        
            .css-17b17hr li {
                margin: 0em 1.2em 0em 1.2em;
                padding: 0px 0em 0px 0.6em;
                font-size: 1rem;
                direction: rtl;
            }
            .css-zt5igj {
                left: calc(0rem);
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
    [page.display_name for page in PAGES],
    label_visibility="collapsed",
)


def display_page(page_display_name: str) -> None:
    with st.container():
        # Find page with this display name and handle errors
        matched_pages = [page for page in PAGES if page.display_name == page_display_name]
        if len(matched_pages) == 0:
            raise RecognizedSiteException("לא מצאנו את הדף שבחרת")
        elif len(matched_pages) > 1:
            raise RecognizedSiteException("נמצאו שני דפים בעלי אותו השם")
        page = matched_pages[0]

        # Display this page
        page.write_title()
        page.write()


def main():
    placeholder = st.empty()
    try:
        with placeholder.container():
            display_page(selected_page_name)
    except Redirect:
        with placeholder.container():
            display_page(selected_page_name)
    except RecognizedSiteException as e:
        with placeholder.container():
            write_error(str(e))
    except Exception as e:
        with placeholder.container():
            write_error("האמת שאנחנו לא עד הסוף מבינים מה קרה ... להלן הפירוט:", str(e))
    finally:
        indent_menu()


if __name__ == '__main__':
    main()
