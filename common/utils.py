import os
import subprocess

from components.error import write_error


def display_name(name: str) -> str:
    name = name.replace("Exercise", "תרגיל")
    name = name.replace("Chapter", "פרק")
    name = name.replace("_", " ")
    return name


TMP_JAVA_FILE = "tmp/A.java"


def try_remove(path: str) -> None:
    try:
        os.remove(path)
    except FileNotFoundError:
        pass


def run_java_program(java_class_name: str, java_code: str) -> str:
    java_path = os.path.join("tmp", f"{java_class_name}.java")
    class_path = os.path.join("tmp", f"{java_class_name}.class")

    with open(java_path, "w") as f:
        f.write(java_code)

    try:
        # TODO: handle unsafe stuff!
        output = subprocess.run(f"javac {java_path}", capture_output=True, shell=True)
        if output.returncode != 0:
            raise Exception("לא הצלחנו לקמפל את הקוד שלך ...")

        output = subprocess.run(f'cd "tmp" && java {java_class_name}', capture_output=True, shell=True)
        if output.returncode != 0:
            raise Exception("הייתה לך שגיאת זמן ריצה ...")
    finally:
        try_remove(java_path)
        try_remove(class_path)
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
