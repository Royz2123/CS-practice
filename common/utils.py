import os
import shutil
import subprocess
import time
import uuid

from components.error import write_error


def display_name(name: str) -> str:
    name = name.replace("Exercise", "תרגיל")
    name = name.replace("Chapter", "פרק")
    name = name.replace("_", " ")
    return name


def try_remove(path: str) -> None:
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        pass


def run_java_program(java_class_name: str, java_code: str) -> str:
    # Save edited code in tmp folder, under generated sub-folder
    if not os.path.exists("tmp"):
        os.mkdir("tmp")
    tmp_sub_folder_name = str(uuid.uuid4())[:8]
    tmp_sub_folder_path = os.path.join("tmp", tmp_sub_folder_name)
    os.mkdir(tmp_sub_folder_path)
    java_path = os.path.join("tmp", tmp_sub_folder_name, f"{java_class_name}.java")

    # Write content to local file
    with open(java_path, "w") as f:
        f.write(java_code)

    try:
        # TODO: handle unsafe stuff!
        # TODO: Change from <br> to different error types

        # Compile the program
        output = subprocess.run(f"javac {java_path}", capture_output=True, shell=True)
        if output.returncode != 0:
            raise Exception(f"לא הצלחנו לקמפל את הקוד שלך ... התקבלה השגיאה הבאה:<br> {output.stderr.decode()}")

        # Run the java program
        output = subprocess.run(
            f'cd "tmp" && cd "{tmp_sub_folder_name}" && java {java_class_name}',
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
