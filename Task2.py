import os
import speech_recognition
from translate import Translator
from tkinter import *
from gtts import gTTS

window = Tk()
window.title("Lets Translate Languages")
window.geometry("500x200")
window.config(bg='light blue')

# img2 = PhotoImage(file='E:\Course Materials\Projects And Certificates\Code Speedy Internship Projects\black-grey-background-free-photo.png')
# label = Label( window,image=img2)
 
Iplang = StringVar()
Trlangchoi = StringVar()

LanguageChoices = {'Hindi','English','French','German','Spanish','Chinese','Kannada'}
Iplang.set('English')
Trlangchoi.set('Hindi')
click_btn= PhotoImage(file='E:\Course Materials\Projects And Certificates\Code Speedy Internship Projects\speaker-microphone-500x500 (2).png',width="80",height="80")
#self.b.config(image=click_btn,width="10",height="10")


def Trans():
    translator = Translator(from_lang= Iplang.get(),to_lang=Trlangchoi.get())
    Translation = translator.translate(Texar.get())
    Outar.set(Translation)
    print(Translation)
    ts = gTTS(Translation)
    ts.save("audio.mp3")
    os.system("audio.mp3")
      
    
NewLangChMenu = OptionMenu(window,Trlangchoi,*LanguageChoices)
Label(window,text="Translated Language").grid(row=0,column=2)
NewLangChMenu.grid(row=1,column=2)

Label(window,text="Text To Be Translated", font= ('Calibri 10 bold')).grid(row=2,column =0)
Texar = StringVar()
TextBox = Entry(window,textvariable=Texar).grid(row=3,column = 0)
 
Label(window,text="Translated Output", font= ('Calibri 10 bold')).grid(row=2,column =2)
Outar = StringVar()
TextBox = Entry(window,textvariable=Outar).grid(row=3,column = 2)

InputLanguageChoiceMenu = OptionMenu(window,Iplang,*LanguageChoices)
Label(window,text="Choose a Language").grid(row=0,column=1)
InputLanguageChoiceMenu.grid(row=1,column=1)
 
But = Button(window,text="The Translated Version",font= ('Calibri 10 bold'),command=Trans, image=click_btn ).grid(row=6,column=1,columnspan = 1)
Label(window,text="Output is in form of voice and text!!").grid(row=6,column=2) 

mainloop()