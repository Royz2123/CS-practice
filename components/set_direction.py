import streamlit as st


def set_direction(css_name: str, direction: str = "RTL") -> None:
    st.markdown(
        f"""
            <style>
            {css_name} {{
              unicode-bidi:bidi-override;
              direction: {direction};
            }}
            </style>
        """,
        unsafe_allow_html=True
    )
