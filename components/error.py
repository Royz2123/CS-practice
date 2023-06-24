import streamlit as st


def write_error(err_msg: str) -> None:
    # TODO: Clear the page
    st.title("😕 משהו השתבש...")
    st.write(err_msg, unsafe_allow_html=True)

    # TODO: Add a contact us part, add also to homepage
    st.write("מוזמנים ליצור איתנו קשר!")
