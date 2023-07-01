from typing import List

import streamlit as st

from common.exceptions import RecognizedSiteException
from webpages.base_page import BasePage
from webpages.chapter_page import ChapterPage


class ExerciseIntoPage(BasePage):
    DISPLAY_NAME = "✏️ תרגילים"
    MENU_INDEX = "0.3"

    def __init__(self, chapters: List[ChapterPage]):
        super(ExerciseIntoPage, self).__init__(ExerciseIntoPage.DISPLAY_NAME, ExerciseIntoPage.MENU_INDEX)
        self.chapters = chapters

    def write(self) -> None:
        st.subheader("פרקים")
        st.markdown("\n".join([f"- {exercise.display_name}" for exercise in self.chapters]))
