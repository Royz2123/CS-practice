import streamlit as st

from components.contact_us import write_contact_us


def write_error(err_msg: str, err_info: str = None) -> None:
    st.title("😕 משהו השתבש...")
    st.write(err_msg, unsafe_allow_html=True)
    if err_info is not None:
        st.error(err_info)
    write_contact_us()
