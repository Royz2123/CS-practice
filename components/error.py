import streamlit as st

from components.contact_us import write_contact_us


def write_error(err_msg: str) -> None:
    # TODO: Clear the page
    st.title("😕 משהו השתבש...")
    st.write(err_msg, unsafe_allow_html=True)

    write_contact_us()
