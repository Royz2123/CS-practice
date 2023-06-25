import os.path

import streamlit as st

from components.center_image import write_center_image


def write_about_page() -> None:
    st.write(f"מוכנים? בואו נתחיל!")
    st.write("קודם כל, תבחרו תרגיל מהתפריט הימני:")
    write_center_image(os.path.join("images", "select_exercise.png"))

    st.write("מיד ייפתח לכם דף התרגיל. קודם כל, תוכלו לצפות ב-PDF עם הוראת התרגיל ע\"י לחיצה על \"לצפייה בהוראות התרגיל\". ייפתח לכם PDF המפרט את הוראות הרגיל:")
    write_center_image(os.path.join("images", "open_exercise_instructions.png"))

    st.write("לאחר שקראתם את הוראות התרגיל, ותכננתם מה הדרך הנכונה למימוש הפתרון, אפשר לגשת לכתיבת הקוד 😄. שימו לב שאתם לא צריכים לצאת מהאתר כדי לממש את הפתרון שלכם - אפשר לעשות הכל דרך האתר! במידה ואתם עדיין מעוניינים להוריד את התרגיל למחשבכם האישי, תוכלו להוריד את כל הקבצים הרלוונטים כ-zip ממש כאן:")
    write_center_image(os.path.join("images", "download_exercise.png"))

    st.write("אנחנו ממליצים לעבוד מהאתר כדי לחסוך התעסקות ב-IDE. יש לרשותכם באתר editor נוח המותאם לשפת JAVA שבו תוכלו לממש את הפתרון שלכם. ה-editor מאותחל עם התבנית של התרגיל כדי שתוכלו ישר להתחיל במימוש עצמו:")
    write_center_image(os.path.join("images", "exercise_template.png"))

    st.write("לרוב, תהיה בתבנית הוראה בסגנון Fill in your solution here, שמסמנת לכם איפה הקוד שלכם אמור להיכתב. לאחר שסיימתם לממש את הפתרון שלכם (אל תשכחו לממש גם את ה-main!), תוכלו להריץ את התוכנה על ידי לחיצה על כפתור Run:")
    write_center_image(os.path.join("images", "run_exercise.png"))

    st.write("האתר יקמפל ויריץ את התוכנה שלכם, ויציג את הפלט שיצא. לאחר שסיימתם לממש את הפתרון שלכם, אנחנו ממליצים שתבדקו את הפתרון שלכם באופן עצמאי ב-main. האם אתם בטוחים בנכונות הפתרון? טיפלתם בכל מקרי הקצה?")
    st.write("לאחר שהשתכנעתם שהפתרון שלכם נכון, אפשר לגשת לבדוק אותו אל מול הטסטים המסופקים בתרגיל. פשוט לחצו על Test והאתר יבדוק את הפתרון שלכם מול הטסטים של התרגיל וידווח כמה טסטים עברתם:")
    write_center_image(os.path.join("images", "test_exercise.png"))

    st.write("אם לא עברתם את כל הטסטים - כנראה משהו לא תקין בפתרון שלכם! נסו להבין מה הבעיה ולתקן. אגב, אם תלחצו על \"להצגת הטסטים של התרגיל\" תוכלו לצפות בטסטים האתר מריץ מול הפתרון שלכם:")
    write_center_image(os.path.join("images", "exercise_tests.png"))

    st.write("שימו ❤️: הטסטים מניחים שלא שיניתם את התבנית של התרגיל! לצורך העניין, אם תשנו את חתימת הפונקציה מהתבנית, הקומפילציה של הטסטים תיכשל:")
    write_center_image(os.path.join("images", "test_error.png"))
