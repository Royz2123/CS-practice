import base64
import os.path
from typing import Dict

import streamlit as st

from common.utils import display_name
from components.editor import write_editor
from components.error import write_error


class Exercise(object):
    PATH_DISPLAY_NAMES = {
        "template_path": "קובץ הטמפלייט",
        "pdf_path": "קובץ ההדרכה",
        "test_java_path": "קובץ הבדיקות",
    }

    def __init__(self, exercise_path: str):
        self.exercise_path = exercise_path
        self.exercise_name = os.path.basename(exercise_path)
        self.display_exercise_name = display_name(self.exercise_name)

        # Save all relevant paths
        self.template_java_path = os.path.join(exercise_path, f"{self.exercise_name}.java")
        self.pdf_path = os.path.join(exercise_path, f"{self.exercise_name}.pdf")
        self.test_java_path = os.path.join(exercise_path, f"Test{self.exercise_name}.java")
        self.all_paths = {
            "template_path": self.template_java_path,
            "pdf_path": self.pdf_path,
            "test_java_path": self.template_java_path
        }
        print(self.all_paths)

        # Make sure that exercise is valid
        self.valid_exercise = True
        for path_name, path in self.all_paths.items():
            if not os.path.exists(path):
                display_path_name = Exercise.PATH_DISPLAY_NAMES[path_name]
                write_error(
                    f"יש לנו בעיה עם התרגיל שבחרתם, לא הצלחנו למצוא את "
                    f"{display_path_name}"
                    f" של התרגיל ולכן לא ניתן לטעון אותו."
                )
                self.valid_exercise = False
                break

        # Load exercise content if valid
        if self.valid_exercise:
            with open(self.template_java_path) as f:
                self.template_java_code = f.read()
                self.template_java_code += "\n\n"

    def write(self) -> Dict[str, str]:
        st.subheader(self.display_exercise_name)
        editor_response = write_editor(self.template_java_code)
        return editor_response


def write_exercise_page(exercise_dir_path: str = "exercises/Exercise_2_1/") -> None:
    # Create exercise instance
    exercise = Exercise(exercise_dir_path)
    if not exercise.valid_exercise:
        return

    # Display exercise
    editor_response = exercise.write()

    # Ignore responses from page reload
    if editor_response["type"] == "":
        return

    # Handle valid editor responses
    # TODO: Run the program
    # TODO: Test the program
    print(editor_response)
