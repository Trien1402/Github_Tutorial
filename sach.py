import pyttsx3
import PyPDF2
sach=open("Trien.pdf","rb")
pdfReader=PyPDF2.PdfFileReader(sach)
pages=pdfReader.numPages
print(pages)
bot=pyttsx3.init()
voices=bot.getProperty("voices")
bot.setProperty("voice",voices[0].id)
page=pdfReader.getPage(3)
text=page.extractText()

bot.say(text)
bot.runAndWait()
