import streamlit as st

from components.body_rtl import set_body_rtl

# set_body_rtl()


def write_home_page() -> None:
    set_body_rtl()

    st.write("# ברוכים הבאים", unsafe_allow_html=True)

    st.header("Sup")

    st.markdown(
        """
ברוכים הבאים!

        **👈 Select a demo from the dropdown on the left** to see some examples
        of what Streamlit can do!

        ### Want to learn more?

        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)

        ### See more complex demos

        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


if __name__ == '__main__':
    write_home_page()
