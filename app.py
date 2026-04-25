import streamlit as st
from PyPDF2 import PdfReader

(page_title="Docuwise", page_icon="📄")

("📄 Docuwise - PDF سے بات کریں")
("اپنی PDF فائل اپلوڈ کریں اور اس سے سوال پوچھیں")

uploaded_file = ("PDF فائل چنیں", type="pdf")

if uploaded_file is not None:
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += ()
    
    ("PDF کامیابی سے اپلوڈ ہو گئی!")
    
    question = ("PDF کے بارے میں سوال پوچھیں:")
    
    if question:
        ("*جواب:*")
        if () in ():
            ("آپ کا سوال PDF میں موجود ہے۔")
        else:
            ("معذرت، یہ معلومات PDF میں نہیں ملی۔")
        
        with ("PDF کا Text دیکھیں"):
            (text[:1000] + "...")
