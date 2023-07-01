import streamlit as st

from components.contact_us import write_contact_us
from webpages.base_page import BasePage


class HomePage(BasePage):
    DISPLAY_NAME = "🏠 עמוד הבית"
    MENU_INDEX = "0.1"

    def __init__(self):
        super(HomePage, self).__init__(HomePage.DISPLAY_NAME, HomePage.MENU_INDEX)

    def write(self) -> None:
        st.subheader("ברוכים הבאים! 👋")
        st.write(
            "אתר זה מכיל מאגר של תרגילים מייצגים מתוך תוכנית הלימודים במדעי המחשב לתלמידי תיכון. התרגילים הללו נבחרו בקפידה, ואמורים לייצר כיסוי על מרבית החומר הנכלל בפרק \"יסודות\" של תוכנית הלימודים (יחידות לימוד 1+2). כרגע האתר תומך בשפת JAVA בלבד, אך בעתיד האתר יתמוך גם בשפת C#.")
        st.write(
            "אנו מאמינים שעבודה מול **טסטים** היא חלק בלתי-נפרד מתהליך העבודה במדעי המחשב. לעיתים קרובות, תוכנות מתנהגות בצורות לא צפויות ועל כן תמיד חשוב לבדוק את הפתרונות שלכם בצורה יסודית. לכן, כל תרגיל שהגדרנו מורכב מ-3 חלקים - קובץ PDF המכיל את הגדרת התרגיל, קובץ JAVA המכיל את התבנית לתרגיל, **וקובץ JAVA אשר מכיל רשימה של טסטים אשר יבדקו את נכונות הפתרון שלכם.**")
        write_contact_us()
