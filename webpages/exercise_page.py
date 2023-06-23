import os
from typing import Dict, Any

import streamlit as st
import streamlit_toggle as tog

from common.utils import display_name, run_java_program
from components.code import write_code
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
        self.tests_name = f"Test{self.exercise_name}"
        self.display_exercise_name = display_name(self.exercise_name)

        # Save all relevant paths
        self.template_java_path = os.path.join(exercise_path, f"{self.exercise_name}.java")
        self.pdf_path = os.path.join(exercise_path, f"{self.exercise_name}.pdf")
        self.test_java_path = os.path.join(exercise_path, f"{self.tests_name}.java")
        self.all_paths = {
            "template_path": self.template_java_path,
            "pdf_path": self.pdf_path,
            "test_java_path": self.template_java_path
        }

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

            with open(self.test_java_path) as f:
                self.test_java_code = f.read()
                self.test_java_code += "\n\n"

    def write_exercise(self) -> Dict[str, Any]:
        # TODO: Improve explanation of every exercise
        st.write("להלן הסבר על התרגיל / קישור ל-PDF")

        # TODO: Download button for all necessary files
        st.write("מוזמנים ללחוץ כאן כדי להוריד את כל החומרים הרלוונטיים לתרגיל")

        # Display tests toggle button
        col1, col2, _ = st.columns(3)
        with col1:
            st.write("הצגת הטסטים")
        with col2:
            display_tests = tog.st_toggle_switch(
                label="",
                key="Key1",
                default_value=False,
                label_after=False,
                inactive_color='#D3D3D3',
                active_color="#11567f",
                track_color="#29B5E8"
            )

        # Displate the code editor

        editor_response = None
        if display_tests:
            # TODO: Make it look more like the editor, with header and copy button. Maybe can bypass editability.
            write_code(self.test_java_code)
        else:
            editor_response = write_editor(self.template_java_code, additional_heading=f"{self.exercise_name}.java")
        return editor_response

    def write_run_response(self, java_code: str) -> None:
        try:
            with st.spinner("מקמפל ומריץ ..."):
                output = run_java_program(self.exercise_name, java_code)
            st.success("התוכנה שלך רצה בהצלחה! להלן הפלט:")
            display_output = "<התוכנה לא הדפיסה כלום>" if not output else output
            write_code(display_output)
        except Exception as e:
            st.error("הרצת התוכנה נכשלה! להלן הפירוט:")
            err_type, err_info = str(e).split("<br>", 1)
            st.error(err_type)
            write_code(err_info)


def write_exercise_page(exercise_dir_path: str) -> None:
    # Create exercise instance
    exercise = Exercise(exercise_dir_path)
    if not exercise.valid_exercise:
        return

    # Display exercise
    editor_response = exercise.write_exercise()

    # Ignore responses from page reload
    if editor_response is None or editor_response["type"] == "":
        return

    # Handle valid editor responses
    if editor_response["type"] == "submit":
        exercise.write_run_response(editor_response["text"])
    elif editor_response["type"] == "test":
        # TODO: Test the program
        # TODO: Move the test file to a common file and not in every exercise
        print("Going to test: ", editor_response)
    else:
        write_error(
            "אנחנו לא מכירים את הפעולה שבחרת - "
            f'{editor_response["type"]}'
        )
