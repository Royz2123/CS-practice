import streamlit as st

from components.set_direction import set_direction


def write_code(code: str, language: str or None = "java") -> None:
    set_direction(".css-l3yxb1", direction="LTR")
    st.code(code, language=language)
