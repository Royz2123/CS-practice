import os.path

import streamlit as st

from components.center_image import write_center_image
from components.contact_us import write_contact_us
from webpages.base_page import BasePage


class TeachersPage(BasePage):
    DISPLAY_NAME = "📌 למורים"
    MENU_INDEX = "9"

    FILE_EXPLANATIONS = [
        "`Exercise_2_4.java` - **קובץ התבנית לתרגיל** - קובץ זה יהיה הטמפלייט שהחניכים יתחילו ממנו את התרגיל. הקובץ יכיל מחלקה אחת ששמה `Exercise_2_4`, שתכיל את כל החתימות לפונקציות שתרצו לספק לתלמידים. שימו לב שאם אתם רוצים שהתבנית תתקמפל עליכם להחזיר ערך כלשהו בתור placeholder למשל `return -1`.",
        "`Exercise_2_4_sol.java` - **קובץ הפתרון לתרגיל** - קובץ זה יכיל את דוגמא לפתרון עבור התרגיל. הוא יכיל מחלקה אחת בשם `Exercise_2_4_sol`. אל תדאגו - התלמידים לא יוכלו לראות קובץ זה באתר. ",
        "`TestExercise_2_4.java` - **קובץ הבדיקות לתרגיל** - קובץ זה יכיל את כל הבדיקות המלוות לתרגיל. הוא יכיל מחלקה אחת בשם `TestExercise_2_4_sol`. המחלקה תכיל קריאות לבחירתכם למתודות שהוגדרו ב-`Exercise_2_4`, ויבדקו את נכונות הפתרון של התלמיד. את הבדיקות יש לממש באמצעות מחלקת `TestingFramework` שכתבנו, אשר אמורה להקל משמעותית על כתיבת הטסטים. ניתן לראות מגוון דוגמאות לשימושים במחלקה בתרגילים הקיימים. ",
        "`Exercise_2_4.docx` & `Exercise_2_4.pdf` - **קובץ הדרכה לתרגיל (WORD אופציונלי אך מומלץ)** - קובץ זה יכיל את ההדרכה שלכם לתרגיל. השתדלו להיצמד לפורמט של התרגילים הקיימים. שימו לב שהאתר עושה שימוש רק בגרסת ה-PDF ולא בגרסת ה-WORD. ",
        "`info.json` - קובץ מידע נלווה לתרגיל - יש להגדיר עוד קובץ קטן שיכיל מידע נלווה שיוצג באתר על התרגיל. כרגע רק צריך למלא את שדה ה`heading` (כותרת תצוגה) של התרגיל.",
    ]

    def __init__(self):
        super(TeachersPage, self).__init__(TeachersPage.DISPLAY_NAME, TeachersPage.MENU_INDEX)

    def write(self) -> None:
        st.write(f"רוצים להעשיר את האתר שלנו בתרגילים נוספים? יאללה! העלאת תרגיל חדש לאתר זה ממש קלי קלות. כל התרגילים של האתר מאוחסנים בפרויקט Github - אתם יותר ממוזמנים ליצור איתנו קשר על מנת שנוכל לפתוח לכם הרשאות צפייה ועריכה 😄 (פרטי ההתקשרות שלנו בתחתית העמוד).")
        st.write("בואו נניח שאתם רוצים לעלות תרגיל ל'פרק 2: מושגי יסודת בתכנות'. לצורך כך, תצטרכו לייצר תיקייה בשם `Exercise_2_X`, כש-`X` יהיה המיספור של התרגיל באתר. לצורך העניין, בואו נניח שאנחנו כותבים את `Exercise_2_4`, שהוא תרגיל 4 בפרק 2.")
        st.write("כעת, צרו תיקייה בשם `Exercise_2_4` במחשבכם האישי, וצרו בתוכה את הקבצים הבאים:")
        st.info("**טיפ:** ממש מומלץ להעתיק את מבנה התיקיות מתרגיל קיים שמזכיר את התרגיל שאתם רוצים לעלות! מוזמנים ליצור איתנו קשר כדי לקבל גישה לדוגמאות הרלוונטיות.")
        st.markdown("\n".join([f"- {file_exp}" for file_exp in TeachersPage.FILE_EXPLANATIONS]))
        st.warning("**שימו ❤️:** כיום, צריך לקרוא לכל הקבצים והמחלקות של התרגיל עם `Exercise_X_Y`, ולא בשמות אינדיקטיביים. בקרוב מאוד נאפשר גם לתת שמות יותר משמעותיים, כאפשרות אופציונלית ב`info.json`")
        st.write("לאחר שיצרתם את כל הקבצים הרלוונטיים, מבנה התיקיות שלכם אמור להיראות כך:")
        write_center_image(os.path.join("images", "exercise_dir.png"))
        st.write("בשלב זה, עליכם ליצור איתנו קשר על מנת שנעלה את התיקייה שלכם לאתר. אנחנו נריץ כמה בדיקות יחד איתכם כדי לראות שכל התרגילים עובדים היטב, וסיימנו!")
        write_contact_us()