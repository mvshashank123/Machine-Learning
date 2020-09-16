import pyttsx3
import PyPDF2

#opens the file
book=open('sample.pdf','rb')

#reads the pdf
pdfReader=PyPDF2.PdfFileReader(book)

#finds the number of pages
pages=pdfReader.numPages

#initializes the speaker
speaker =pyttsx3.init()

# this loops through all the pages
for num in range(0,pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    print(text)
    speaker.say(text)
    speaker.runAndWait()