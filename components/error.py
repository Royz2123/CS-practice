import streamlit as st


def write_error(err_msg: str) -> None:
    # TODO: Clear the page
    st.title("😕 משהו השתבש...")
    st.write(err_msg)

    # TODO: Add a contact us part
    st.write("מוזמנים ליצור איתנו קשר!")
