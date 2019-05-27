from tkinter import *
import translator

def search_command():
    return translator.word


window=Tk()
window.title("ist alles gut")
window.geometry('350x200')

lbl=Label(window,text="Type in a word in English: ")
lbl.grid(column=0,row=0)

word_text=StringVar()
txt=Entry(window,width=10,textvariable=word_text)
txt.grid(column=1,row=0)

result=Label(window,text=translator.translate(translator.word))
result.grid(row=1,column=1)

# def clicked():
#     lbl.configure(text="Button was clicked")

btn=Button(window,text="Translate",command=search_command,bg="orange",fg="red")
btn.grid(column=2,row=0)



window.mainloop()
