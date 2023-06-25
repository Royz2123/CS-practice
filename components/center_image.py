import os.path

import streamlit as st

CENTER_RATIOS = [0.2, 0.6, 0.2]


def write_center_image(img_path: str) -> None:
    _, col2, _ = st.columns(CENTER_RATIOS)
    with col2:
        st.image(img_path)
