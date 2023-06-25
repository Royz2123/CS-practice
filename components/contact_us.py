import streamlit as st


def write_contact_us() -> None:
    st.divider()

    st.subheader("צרו קשר ☎️")
    st.write(
        "אתם יותר ממוזמנים לפנות אלינו בכל עניין! אם עלתה לכם שאלה / תקלה באתר, או שאולי בא לכם לעזור לנו לשפר אותו, אתם ממש מוזמנים ליצור איתנו קשר 😄."
    )
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("**רועי זהר**")
    with col2:
        st.write("📞 053-277-9499")
    with col3:
        st.write("✉️ roy.zohar.40@gmail.com")
