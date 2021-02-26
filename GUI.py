from tkinter import *

HEIGHT = 300
WIDTH = 150

window = Tk()
window.title("Practice 0.RSA")
window.geometry(str(HEIGHT)+'x'+str(WIDTH))
window.resizable(0,0)

frame = Frame(window,background="#23262E")
frame.pack(fill="both", expand=True)

label = Label(frame, text="Choose your option:",fg="#fff",background="#23262E",font=("Arial",14))
label.pack()


#None option
option = IntVar()

radioButton1 = Radiobutton(frame,text="Encrypt",variable=option,value=1,background="#23262E",fg="#fff",font=("Arial",12))
radioButton1.pack()

radioButton2 = Radiobutton(frame,text="Decrypt",variable=option,value=2,background="#23262E",fg="#fff",font=("Arial",12))
radioButton2.pack()

selectButton = Button(frame,text="select",bd=0,fg="#fff",bg="#7A5FEE",font=("Arial",12))
selectButton.pack()


window.mainloop()