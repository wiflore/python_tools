import PyPDF2

pdfFileObj = open('ViewPDF.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
pageObj = pdfReader.getPage(0)
p1 = pageObj.extractText()
print(p1)

pdfFileObj = open('Ficha Técnica Class Alta Líquidez 300617.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
pageObj = pdfReader.getPage(0)
p1 = pageObj.extractText()
print(p1)
