import json
import os
from json import JSONDecodeError
from typing import Literal
from zipfile import ZipFile

import streamlit as st
import streamlit_toggle as tog

from common.exceptions import RecognizedSiteException, JavaProgramException, InvalidExerciseException
from common.java_class import JavaClass
from common.utils import run_java_program, create_tmp_sub_folder, try_remove
from components.code import write_code
from components.editor import write_editor
from components.pdf_file import write_pdf
from webpages.base_page import BasePage

TESTING_FRAMEWORK_PATH = os.path.join("exercises", "TestingFramework.java")
TESTING_FRAMEWORK_CLASS = JavaClass("TestingFramework", class_path=TESTING_FRAMEWORK_PATH)


class ExercisePage(BasePage):
    REQUIRED_INFO_FIELDS = ["heading"]

    PATH_DISPLAY_NAMES = {
        "template_path": "קובץ התבנית",
        "pdf_path": "קובץ ההדרכה",
        "test_java_path": "קובץ הטסטים",
    }

    def __init__(self, dir_name: str, chapter_dir_name: str):
        # Validate exercise name
        if not ExercisePage.valid_dir_name(dir_name):
            raise InvalidExerciseException(f"Invalid exercise directory name: {dir_name}")

        # Create base attributes
        self.dir_name = dir_name
        self.chapter_dir_name = chapter_dir_name
        self.dir_path = os.path.join("exercises", chapter_dir_name, dir_name)
        _, self.chapter_num, self.num = dir_name.split("_", 2)

        # Validate exercise path
        if not os.path.isdir(self.dir_path):
            raise InvalidExerciseException(f"Exercise {self.dir_name} has an invalid path: {self.dir_path}")

        # Add info.json data to exercise
        info_path = os.path.join(self.dir_path, "info.json")
        if not os.path.exists(info_path):
            raise InvalidExerciseException(f"Exercise {self.dir_name} has no info.json file included")
        with open(info_path, encoding="utf-8") as f:
            try:
                info_data = json.load(f)
            except JSONDecodeError as e:
                raise InvalidExerciseException(f"Exercise {self.dir_name} has an invalid info.json file - {e}")
        for field in ExercisePage.REQUIRED_INFO_FIELDS:
            if field not in info_data:
                raise InvalidExerciseException(
                    f"Exercise {self.dir_name}'s info.json is missing required field {field}"
                )
        self.heading = info_data["heading"]

        # Call super method
        super(ExercisePage, self).__init__(self.get_display_name(), f"{self.chapter_num}.{self.num}")

        # Define all exercise sub-paths
        self.tests_name = f"Test{self.dir_name}"
        self.template_java_path = os.path.join(self.dir_path, f"{self.dir_name}.java")
        self.pdf_path = os.path.join(self.dir_path, f"{self.dir_name}.pdf")
        self.test_java_path = os.path.join(self.dir_path, f"{self.tests_name}.java")
        self.all_paths = {
            "template_path": self.template_java_path,
            "pdf_path": self.pdf_path,
            "test_java_path": self.test_java_path
        }

        # Make sure that all exercise sub-paths exist
        for path_name, path in self.all_paths.items():
            if not os.path.exists(path):
                raise InvalidExerciseException(
                    f"יש לנו בעיה עם התרגיל שבחרתם "
                    f"({self.display_name})"
                    f". לא הצלחנו למצוא את "
                    f"{ExercisePage.PATH_DISPLAY_NAMES[path_name]}"
                    f" של התרגיל ולכן לא הצלחנו לטעון אותו."
                )

        # Load exercise content
        with open(self.template_java_path, encoding="utf-8") as f:
            self.template_java_code = f.read()
            self.template_java_code += "\n\n"
        with open(self.test_java_path, encoding="utf-8") as f:
            self.test_java_code = f.read()
            self.test_java_code += "\n\n"
        self.test_java_class = JavaClass(self.tests_name, class_code=self.test_java_code)

    def get_display_name(self) -> str:
        return f"📄 {self.chapter_num}.{self.num}: {self.heading}"

    @staticmethod
    def valid_dir_name(dir_name: str):
        return dir_name.startswith("Exercise") or dir_name.count("_") < 2

    def write(self) -> None:
        # Display exercise explanation
        with st.expander("לצפייה בהוראות התרגיל"):
            write_pdf(self.pdf_path)
        st.write("")

        # Display download and toggle button
        self.write_download_exercise()
        display_tests = self.write_toggle_code_switch()

        # Displate the code editor
        if display_tests:
            editor_response = write_editor(
                self.test_java_code,
                additional_heading=f"{self.tests_name}.java",
                read_only=True,
            )
        else:
            editor_response = write_editor(
                self.template_java_code,
                additional_heading=f"{self.dir_name}.java"
            )

        # Ignore responses from page reload
        if editor_response is None or editor_response["type"] == "":
            return

        # Handle valid editor responses
        if editor_response["type"] not in ["submit", "test"]:
            raise RecognizedSiteException(
                "אנחנו לא מכירים את הפעולה שבחרת - "
                f'{editor_response["type"]}'
            )
        self.write_output(editor_response["text"], editor_response["type"])

    def write_download_exercise(self):
        # Create tmp sub folder for zip file
        tmp_sub_folder_path = create_tmp_sub_folder()
        zip_file_name = f"{self.dir_name}.zip"
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

    @staticmethod
    def write_toggle_code_switch() -> bool:
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

    def write_output(self, java_code: str, run_type: Literal["submit", "test"]) -> None:
        try:
            with st.spinner("מקמפל ומריץ ..."):
                if run_type == "submit":
                    output = run_java_program(JavaClass(self.dir_name, class_code=java_code))
                else:
                    output = run_java_program(
                        self.test_java_class,
                        other_java_classes=[
                            JavaClass(self.dir_name, class_code=java_code),
                            TESTING_FRAMEWORK_CLASS
                        ]
                    )

            if run_type == "submit":
                st.info("התוכנה שלך התקמפלה ורצה בהצלחה! להלן הפלט:")
            elif output == "":
                raise RecognizedSiteException("נראה שהטסטים שהודפסו לא בפורמט הנכון")
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
        except JavaProgramException as e:
            st.error("הרצת התוכנה נכשלה! להלן הפירוט:")
            st.error(str(e))
            write_code(e.err_info, language=None)
