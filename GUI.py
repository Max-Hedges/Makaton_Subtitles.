from tkinter import font
from tkinter import *



def Load_Gif():
    import TextToGifs
    TextToGifs.main()

def Load_GUI():
    
    Start = Tk()
    Start.configure(bg="#9c1912")
    Start.title("Subtitles")
    helv = font.Font(family="Helvitica",size=25,weight="bold")
    lbl = Label(Start, text = "Choose your language and press Start to go",font = helv,fg="#d0d278",bg="#9c1912")
    lang = Listbox(Start, font = helv,bg="#c62f18",fg="#d0d278",borderwidth=0,highlightthickness=0)
    lang.insert(1,"Makaton")
    lang.insert(2,"BSL")
    lang.insert(3,"ASL")
    go = Button(Start, text = "START!", command = Load_Gif, font = helv,fg="#E37435")
    lbl.pack()
    lang.pack()
    go.pack()
    Start.mainloop()

Load_GUI()
