import streamlit as st


def write_code(code: str, language: str or None = "java") -> None:
    st.markdown(
        """
            <style>
            .css-l3yxb1 {
              unicode-bidi:bidi-override;
              direction: LTR;
            }
            </style>
        """,
        unsafe_allow_html=True
    )
    st.code(code, language=language)
