import os
import shutil
import subprocess
import uuid
from typing import Dict, List

from common.java_class import JavaClass


def display_name(name: str) -> str:
    if name.startswith("Exercise"):
        _, chapter_num, exercise_num = name.split("_", 2)
        return f"📄 פרק {chapter_num}, תרגיל {exercise_num}"
    elif name.startswith("Chapter"):
        _, chapter_num = name.split("_", 1)
        return f"📂 פרק {chapter_num}"
    else:
        raise Exception(f"Unrecognized name for display - {name}")


def try_remove(path: str) -> None:
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        pass


def create_tmp_sub_folder() -> str:
    """
    Creates a temporary sub folder under tmp

    :return:
    """
    if not os.path.exists("tmp"):
        os.mkdir("tmp")
    tmp_sub_folder_name = str(uuid.uuid4())[:8]
    tmp_sub_folder_path = os.path.join("tmp", tmp_sub_folder_name)
    os.mkdir(tmp_sub_folder_path)
    return tmp_sub_folder_path


def run_java_program(
        main_java_class: JavaClass,
        other_java_classes: List[JavaClass] = None
) -> str:
    """
    This method takes the given java classes, compiles them and runs :)

    :param main_java_class:
    :param other_java_classes:
    :return:
    """

    # Default java_classes is empty list
    if other_java_classes is None:
        other_java_classes = []

    # Create sub-folder under tmp folder for all the code
    tmp_sub_folder_path = create_tmp_sub_folder()

    # Save all the java classes under this folder
    for java_class in [main_java_class] + other_java_classes:
        java_class.save_class(tmp_sub_folder_path)
    tmp_sub_folder_java_files = os.path.join(tmp_sub_folder_path, "*.java")

    # Compile and run
    try:
        # TODO: handle unsafe stuff!
        # TODO: Change from <br> to different error types

        # Compile the program
        output = subprocess.run(f"javac {tmp_sub_folder_java_files}", capture_output=True, shell=True)
        if output.returncode != 0:
            raise Exception(f"לא הצלחנו לקמפל את הקוד שלך ... התקבלה השגיאה הבאה:<br> {output.stderr.decode()}")

        # Run the java program
        output = subprocess.run(
            f'cd "{tmp_sub_folder_path}" && java {main_java_class.class_name}',
            capture_output=True,
            shell=True
        )
        if output.returncode != 0:
            raise Exception(f"הייתה לך שגיאת זמן ריצה ... התקבלה השגיאה הבאה:<br> {output.stderr.decode()}")
    finally:
        try_remove(tmp_sub_folder_path)
    return output.stdout.decode()


if __name__ == '__main__':
    run_java_program(
        "A",
        """
        class A {
            public static void main(String args[]){
                System.out.println("I am in Java Program");
            }
        }   
        """
    )
