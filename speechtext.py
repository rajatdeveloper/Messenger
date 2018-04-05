import string
import speech_recognition as sr
import smtplib
import xlrd
import datetime
sender = input()
passward = input()
receiver = input()
mail = smtplib.SMTP()
mail.connect('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()  # use to make secure connection
mail.login(sender,passward)
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
    try:
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
        mail.sendmail(sender,receive,r.recognize_google(audio))
    except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
mail.close()
