import fitz  # PyMuPDF
import docx
import io

def read_pdf(file):
    file_stream = file.read()
    with fitz.open(stream=file_stream, filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text

def read_docx(file):
    doc = docx.Document(io.BytesIO(file.read()))
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text

def read_txt(file):
    return file.read().decode("utf-8")
