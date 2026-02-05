import pdfplumber
from docx import Document

def load_file(file):
    filename = file.name.lower()

    if filename.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                if page.extract_text():
                    text += page.extract_text() + "\n"
        return text

    elif filename.endswith(".docx"):
        doc = Document(file)
        return "\n".join([para.text for para in doc.paragraphs])

    elif filename.endswith(".txt"):
        return file.read().decode("utf-8")

    else:
        raise ValueError("Unsupported file format")
