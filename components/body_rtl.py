import streamlit as st


def set_body_rtl() -> None:
    st.markdown(
        """
            <style>
            body {
              unicode-bidi:bidi-override;
              direction: RTL;
            }
            </style>
        """,
        unsafe_allow_html=True
    )
