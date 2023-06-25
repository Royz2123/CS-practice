import base64
import streamlit as st


def write_pdf(pdf_path: str) -> None:
    with open(pdf_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f"""
        <iframe 
            src="data:application/pdf;base64,{base64_pdf}#toolbar=0&navpanes=0&scrollbar=0" 
            width="100%" height="300px" type="application/pdf"
        >
        </iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)
