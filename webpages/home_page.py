import streamlit as st

from components.contact_us import write_contact_us


def write_home_page() -> None:
    pdf_display = f"""
        <embed
          class="pdfobject"
          type="application/pdf"
          title="Embedded PDF"
          src="https://africau.edu/images/default/sample.pdf"
          style="overflow: auto; width: 100%; height: 100%;">            
    """
    #            src="data:application/pdf;base64,{base64_pdf}

    st.markdown(pdf_display, unsafe_allow_html=True)

    st.subheader("ברוכים הבאים! 👋")
    st.write(
        "אתר זה מכיל מאגר של תרגילים מייצגים מתוך תוכנית הלימודים במדעי המחשב לתלמידי תיכון. התרגילים הללו נבחרו בקפידה, ואמורים לייצר כיסוי על מרבית החומר הנכלל בפרק \"יסודות\" של תוכנית הלימודים (יחידות לימוד 1+2). כרגע האתר תומך בשפת JAVA בלבד, אך בעתיד האתר יתמוך גם בשפת C#.")
    st.write(
        "אנחנו מאמינים שעבודה מול **טסטים** זה חלק בלתי-נפרד מתהליך העבודה במדעי המחשב. לעיתים קרובות, תוכנות מתנהגות בצורות לא צפויות ועל כן תמיד חשוב לבדוק את הפתרונות שלכם בצורה יסודית. לכן, כל תרגיל שהגדרנו מורכב מ-3 חלקים - קובץ PDF המכיל את הגדרת התרגיל, קובץ JAVA המכיל את התבנית לתרגיל, **וקובץ JAVA אשר מכיל רשימה של טסטים אשר יבדקו את נכונות הפתרון שלכם.**")
    write_contact_us()


if __name__ == '__main__':
    write_home_page()
