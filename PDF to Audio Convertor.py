# importing the modules
import PyPDF2
import pyttsx3

# put the path of pdf here

path = open('IRJMETS437579-converted-converted.pdf', 'rb')

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(path)

# the page with which you want to start
# this will read the page of 25th page.
from_page = pdfReader.getPage(0)
#print(from_page)

# extracting the text from the PDF
text = from_page.extractText()
print(text)

# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
