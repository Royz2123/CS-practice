import json
import os
from json import JSONDecodeError
from typing import List

import streamlit as st

from common.exceptions import InvalidChapterException
from webpages.base_page import BasePage
from webpages.exercise_page import ExercisePage


class ChapterPage(BasePage):
    REQUIRED_INFO_FIELDS = ["heading", "goals"]

    def __init__(self, dir_name: str, exercises: List[ExercisePage]):
        # Validate chapter name
        if not ChapterPage.valid_dir_name(dir_name):
            raise InvalidChapterException(f"Invalid chapter directory name: {dir_name}")

        # Create base attributes
        self.dir_name = dir_name
        self.exercises = exercises
        self.dir_path = os.path.join("exercises", dir_name)
        self.num = dir_name.split("_", 1)[1]

        # Validate chapter path
        if not os.path.isdir(self.dir_path):
            raise InvalidChapterException(f"Chapter {self.dir_name} has an invalid path: {self.dir_path}")

        # Add info.json data to chapter
        info_path = os.path.join(self.dir_path, "info.json")
        if not os.path.exists(info_path):
            raise InvalidChapterException(f"Chapter {self.dir_name} has no info.json file included")
        with open(info_path, encoding="utf-8") as f:
            try:
                info_data = json.load(f)
            except JSONDecodeError as e:
                raise InvalidChapterException(f"Chapter {self.dir_name} has an invalid info.json file - {e}")
        for field in ChapterPage.REQUIRED_INFO_FIELDS:
            if field not in info_data:
                raise InvalidChapterException(f"Chapter {self.dir_name}'s info.json is missing required field {field}")
        self.heading = info_data["heading"]
        self.goals = info_data["goals"]
        self.content = info_data.get("content", "")

        # Call super method
        super(ChapterPage, self).__init__(self.get_display_name(), f"{self.num}")

    @staticmethod
    def valid_dir_name(dir_name: str):
        return dir_name.startswith("Chapter") and "_" in dir_name

    def get_display_name(self) -> str:
        return f"📂 פרק {self.num}: {self.heading}"

    def write(self) -> None:
        st.subheader("יעדים")
        st.markdown(self.goals)

        st.subheader("תרגילים")
        st.markdown("\n".join([f"- {exercise.display_name}" for exercise in self.exercises]))

        st.subheader("תכנים")
        st.markdown(self.content, unsafe_allow_html=True)
