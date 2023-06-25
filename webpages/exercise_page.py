import os
from typing import Dict, Any, Literal
from zipfile import ZipFile

import streamlit as st
import streamlit_toggle as tog

from common.java_class import JavaClass
from common.utils import display_name, run_java_program, create_tmp_sub_folder, try_remove
from components.code import write_code
from components.editor import write_editor
from components.error import write_error

TESTING_FRAMEWORK_PATH = os.path.join("exercises", "TestingFramework.java")
TESTING_FRAMEWORK_CLASS = JavaClass("TestingFramework", class_path=TESTING_FRAMEWORK_PATH)


class Exercise(object):
    PATH_DISPLAY_NAMES = {
        "template_path": "קובץ התבנית",
        "pdf_path": "קובץ ההדרכה",
        "test_java_path": "קובץ הטסטים",
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
            "test_java_path": self.test_java_path
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

            self.test_java_class = JavaClass(self.tests_name, class_code=self.test_java_code)

    def write_download_exercise(self):
        # Create tmp sub folder for zip file
        tmp_sub_folder_path = create_tmp_sub_folder()
        zip_file_name = f"{self.exercise_name}.zip"
        tmp_zip_file_path = os.path.join(tmp_sub_folder_path, zip_file_name)

        try:
            # Create zip file with all the exercise
            exercise_zip = ZipFile(tmp_zip_file_path, 'w')
            for file_path in self.all_paths.values():
                exercise_zip.write(file_path, arcname=os.path.basename(file_path))
            exercise_zip.write(TESTING_FRAMEWORK_PATH, arcname=os.path.basename(TESTING_FRAMEWORK_PATH))
            exercise_zip.close()

            # Create zip download button
            with open(tmp_zip_file_path, "rb") as f:
                col1, col2, _ = st.columns(3)

                with col1:
                    st.write("להורדת קבצי התרגיל:")
                with col2:
                    st.download_button(
                        'הורדה',
                        f.read(),
                        file_name=zip_file_name,
                        mime="application/zip"
                    )
        finally:
            try_remove(tmp_sub_folder_path)

    def write_toggle_code_switch(self) -> bool:
        col1, col2, _ = st.columns(3)
        with col1:
            st.write("להצגת הטסטים של התרגיל:")
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
        return display_tests

    def write_exercise(self) -> Dict[str, Any]:
        # TODO: Improve explanation of every exercise
        st.write("להלן הסבר על התרגיל / קישור ל-PDF")

        # Display download and toggle button
        self.write_download_exercise()
        display_tests = self.write_toggle_code_switch()

        # Displate the code editor
        editor_response = None
        if display_tests:
            editor_response = write_editor(
                self.test_java_code,
                additional_heading=f"{self.tests_name}.java",
                read_only=True,
            )
        else:
            editor_response = write_editor(
                self.template_java_code,
                additional_heading=f"{self.exercise_name}.java"
            )
        return editor_response

    def write_response(self, java_code: str, run_type: Literal["submit", "test"]) -> None:
        try:
            with st.spinner("מקמפל ומריץ ..."):
                if run_type == "submit":
                    output = run_java_program(JavaClass(self.exercise_name, class_code=java_code))
                else:
                    output = run_java_program(
                        self.test_java_class,
                        other_java_classes=[
                            JavaClass(self.exercise_name, class_code=java_code),
                            TESTING_FRAMEWORK_CLASS
                        ]
                    )

            if run_type == "submit":
                st.success("התוכנה שלך רצה בהצלחה! להלן הפלט:")
            else:
                first_line = output.splitlines()[0]
                _, passed_tests = first_line.split(": ", 1)
                passed, overall = passed_tests.split("/", 1)

                if passed == overall:
                    st.success(
                        "התוכנה שלך עברה את כל הטסטים ("
                        + passed_tests
                        + ")! להלן הפלט:"
                    )
                elif passed == "0":
                    st.error(
                        "התוכנה שלך לא עברה אף טסט ("
                        + passed_tests
                        + ") ... להלן הפלט:"
                    )
                else:
                    st.warning(
                        "התוכנה שלך עברה רק חלק מהטסטים ("
                        + passed_tests
                        + "). להלן הפלט:"
                    )

            # Display output in either case
            display_output = "<התוכנה לא הדפיסה כלום>" if not output else output
            write_code(display_output, language=None)
        except Exception as e:
            st.error("הרצת התוכנה נכשלה! להלן הפירוט:")
            err_type, err_info = str(e).split("<br>", 1)
            st.error(err_type)
            write_code(err_info, language=None)


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
    # TODO: Organize all the exercises to this new format
    if editor_response["type"] not in ["submit", "test"]:
        write_error(
            "אנחנו לא מכירים את הפעולה שבחרת - "
            f'{editor_response["type"]}'
        )
    exercise.write_response(editor_response["text"], editor_response["type"])
