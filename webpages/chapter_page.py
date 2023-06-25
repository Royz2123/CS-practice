import streamlit as st

from common.utils import display_name


def write_chapter_page(chapter_dir_name: str) -> None:
    # TODO: Add explanations for every chapter
    st.write(f"להלן הסבר על {display_name(chapter_dir_name)}")
