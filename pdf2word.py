# pip install pdf2docx #安装依赖库
from pdf2docx import Converter

pdf_file = r'/home/g/Downloads/晚清沧海事（下卷）.pdf'
docx_file = r'/home/g/Downloads/晚清沧海事（下卷）.docx'

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()