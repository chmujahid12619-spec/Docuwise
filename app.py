import streamlit as st
from PyPDF2 import PdfReader

st.set_page_config(page_title="Docuwise", page_icon="📄")

st.title("📄 Docuwise - PDF سے بات کریں")
st.write("اپنی PDF فائل اپلوڈ کریں اور اس سے سوال پوچھیں")

st.file_uploader("PDF فائل چنیں", type="pdf")

if uploaded_file is not None:
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    st.success("PDF کامیابی سے اپلوڈ ہو گئی!")
    
    question = st.text_input("PDF کے بارے میں سوال پوچھیں:")
    
    if question: gv
        st.write("*جواب:*")
        if question.lower() in text.lower():v
            st.info("آپ کا سوال PDF میں موجود ہے۔")
        else:
            st.warning("معذرت، یہ معلومات PDF میں نہیں ملی۔")
        
        with st.expander("PDF کا Text دیکھیں"):
            st.write(text[:1000] + "...")
