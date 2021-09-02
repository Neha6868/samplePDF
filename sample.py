from PyPDF2 import PdfFileReader

# open the PDF file mypdf
pdfFile = open('sample.pdf', 'rb')

# create PDFFileReader object to read the file
pdfReader = PdfFileReader(pdfFile)


numOfPages = pdfReader.getNumPages()

for i in range(0, numOfPages):
	pageObj = pdfReader.getPage(i)
	print(pageObj.extractText())
	
# close the PDF file object
pdfFile.close()