from tkinter import *

HEIGHT = 300
WIDTH = 270
background_color = "#23262E"
white = "#fff"
select_color = "#7A5FEE"
show_inputs = False
last_option = 0

def selectButton_function(option):
  
  global label_priv_key
  global input_priv_key
  global label_public_key
  global input_public_key
  global encryptButton
  global label_space
  
  global show_inputs
  global last_option
  if(last_option != option and not show_inputs):    
    show_inputs = True
    generateInputWigets()
    
  elif(last_option != option and show_inputs):
    destroyWidgets(label_priv_key,label_public_key,input_priv_key,input_public_key,encryptButton,label_space)
    generateInputWigets()    
  
  if(option==1 and last_option != option):
    #Encrypt     
    setInputText(input_priv_key,"Hola")    
    encryptButton = Button(frame,height=1,text="Encrypt",bd=0,fg=white,bg=select_color,font=("Arial",12))
    encryptButton.pack()    
  elif(option == 2 and last_option != option):
    #Decrypt    
    encryptButton = Button(frame,height=1,text="Decrypt",bd=0,fg=white,bg=select_color,font=("Arial",12))
    encryptButton.pack()
  
  last_option = option
  
def setInputText(input_entry,text):
  input_entry.delete(0,END)
  input_entry.insert(0,text)

def destroyWidgets(*widgets):
  for i in widgets:
    i.destroy()
    
def generateInputWigets():
  global label_priv_key
  global input_priv_key
  global label_public_key
  global input_public_key
  global encryptButton
  global label_space
  
  label_priv_key = Label(frame,text="Private Key:",bg=background_color,fg=white,font=("Arial",12))
  label_priv_key.pack()
  input_priv_key = Entry(frame,text="")
  input_priv_key.pack()

  label_public_key = Label(frame,text="Public Key:",bg=background_color,fg=white,font=("Arial",12))
  label_public_key.pack()
  input_public_key = Entry(frame,text="")
  input_public_key.pack() 
  label_space = Label(frame,text="",bg=background_color)
  label_space.pack()

window = Tk()
window.title("Practice 0.RSA")
window.geometry(str(HEIGHT)+'x'+str(WIDTH))
window.resizable(0,0)

frame = Frame(window,background=background_color)
frame.pack(fill="both", expand=True)

label_opt = Label(frame, text="Choose your option:",fg=white,bg=background_color,font=("Arial",14))
label_opt.pack()

option = IntVar()

radioButton1 = Radiobutton(frame,text="Encrypt",variable=option,value=1,bg=background_color,selectcolor=select_color,fg=white,font=("Arial",12))
radioButton1.pack()

radioButton2 = Radiobutton(frame,text="Decrypt",variable=option,value=2,bg=background_color,selectcolor=select_color,fg=white,font=("Arial",12))
radioButton2.pack()

selectButton = Button(frame,text="select",bd=0,fg=white,bg=select_color,font=("Arial",12),command=lambda:selectButton_function(option.get()))
selectButton.pack()

label_priv_key = None
input_priv_key = None
label_public_key = None
input_public_key = None
encryptButton = None
label_space = None
window.mainloop()