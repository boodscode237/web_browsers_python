import PyPDF2
import os

os.chdir('/home/abodo/Documents/webbrowser_python/pfdSheet/')
pdfFile = open('meetingminutes1.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)
num_page = reader.numPages
page = reader.getPage
# print(page(0).extractText())

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())

# function to combine 2 pdf files in a new file

pdf1File=open('meetingminutes1.pdf', 'rb')
pdf2File=open('meetingminutes2.pdf', 'rb')
reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)

# write a new file from the two files
writer = PyPDF2.PdfFileWriter()

for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

output = open('combienedpdfs.pdf', 'wb')
writer.write(output)
output.close()
pdf1File.close()
pdf2File.close()