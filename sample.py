from PyPDF2 import PdfFileReader


pdfFile = open('sample.pdf', 'rb')
pdfReader = PdfFileReader(pdfFile)
numOfPages = pdfReader.getNumPages()

for i in range(0, numOfPages):
	pageObj = pdfReader.getPage(i)
	print(pageObj.extractText())
	
pdfFile.close()