import os
import glob
import PyPDF3 as pyPDF
import pikepdf

#def extractContent(content = ""):
    #fileNames = []
    #numPageBooks = []
    #for files in glob.glob("Resource/*.pdf"):
    #    fileNames.append(files)
    #for i in range(len(fileNames)):
    #    pdfFile = open(fileNames[i], 'rb')
    #    pdfFileReader = PdfFileReader(pdfFile)
    #    if pdfFileReader.isEncrypted:
    #        try:
    #            pdfFileReader.decrypt('')
    #            print('File Decrypted (PyPDF2)')
    #        except:
    #            command = ("copy "+ fileNames[i] +
    #                " Resource/temp.pdf; qpdf --password='' --decrypt Resource/temp.pdf " + fileNames[i]
    #                + "; del Resource/temp.pdf")
    #            os.system(command)
    #            print('File Decrypted (qpdf)')
    #        pdfFile = open(fileNames[i])
    #        pdfFileReader = PdfFileReader(pdfFile)
    #    else:
    #        print('File Not Encrypted')
    #    numPageBooks.append(pdfFileReader.numPages)
    #print numPageBooks

# pdf = pikepdf.open('Resource/Outlaws of the Marshalso.pdf')
# num_pages = len(pdf.pages)
# pdf.save("out.pdf")
# pdfReader = pyPDF.PdfFileReader("out.pdf")
# print(pdfReader.numPages)

def extractContent(content = ""):
    fileNames = []
    # numPageBooks = []
    pdfFileText = []
    pdfFileReader = ''
    for files in glob.glob("Resource/*.pdf"):
        fileNames.append(files)
    for i in range(len(fileNames)):
        pdfFile = open(fileNames[i], 'rb')
        pdfFileReader = pyPDF.PdfFileReader(fileNames[i])
        if(pdfFileReader.isEncrypted):
            pdfFile = pikepdf.open(fileNames[i])
            #pdfFile.save(fileNames[i])
            print("%s decrypted!" %fileNames[i])
            pdfFileReader = pyPDF.PdfFileReader(fileNames[i])
        #numPageBooks.append(pdfFileReader.numPages)
        pdfText = pdfFileReader.getPage(100)
        pdfText = pdfText.extractText()
        pdfFileText.append(pdfText)
        print(pdfFileText)
extractContent()
