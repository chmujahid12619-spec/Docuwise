import streamlit as st
from PyPDF2 import PdfReader

http://st.set_page_config(page_title="Docuwise", page_icon="📄")

http://st.title("📄 Docuwise - PDF سے بات کریں")
http://st.write("اپنی PDF فائل اپلوڈ کریں اور اس سے سوال پوچھیں")

uploaded_file = http://st.file_uploader("PDF فائل چنیں", type="pdf")

if uploaded_file is not None:
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += http://page.extract_text()
    
    http://st.success("PDF کامیابی سے اپلوڈ ہو گئی!")
    
    question = http://st.text_input("PDF کے بارے میں سوال پوچھیں:")
    
    if question:
        http://st.write("*جواب:*")
        if http://question.lower() in http://text.lower():
            http://st.info("آپ کا سوال PDF میں موجود ہے۔")
        else:
            http://st.warning("معذرت، یہ معلومات PDF میں نہیں ملی۔")
        
        with http://st.expander("PDF کا Text دیکھیں"):
            http://st.write(text[:1000] + "...")
