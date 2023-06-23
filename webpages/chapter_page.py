import streamlit as st


def write_chapter_page(chapter_dir_path: str) -> None:
    st.write(f"להלן הסבר על הפרק {chapter_dir_path}")
