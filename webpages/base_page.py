import streamlit as st


class BasePage(object):
    def __init__(self, display_name: str, menu_index: str):
        self.display_name = display_name
        self.menu_index = menu_index

    def __repr__(self):
        return f"Page: {self.display_name}\tMenu Index: {self.menu_index}"

    def write(self) -> None:
        raise NotImplementedError("Page must implement write method")

    def write_title(self) -> None:
        st.title(self.display_name)
        st.divider()
