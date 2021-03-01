from tkinter import *

class GUI():  

  HEIGHT = 300
  WIDTH = 270
  background_color = "#23262E"
  white = "#fff"
  select_color = "#7A5FEE"
  show_inputs = False
  last_option = 0
  window = None
  frame = None
  
  label_priv_key = None
  input_priv_key = None
  label_public_key = None
  input_public_key = None
  encryptButton = None
  label_space = None

  
  def __init__(self):
    self.window = Tk()
    self.window.title("Practice 0.RSA")
    self.window.geometry(str(self.HEIGHT)+'x'+str(self.WIDTH))
    self.window.resizable(0,0)

    self.frame = Frame(self.window,
                  background=self.background_color
                  )
    self.frame.pack(fill="both",
               expand=True
               )

    self.label_opt = Label(self.frame, 
                           text="Choose your option:",
                           fg=self.white,
                           bg=self.background_color,
                           font=("Arial",14)
                           )
    self.label_opt.pack()

    option = IntVar()

    self.radioButton1 = Radiobutton(self.frame,
                               text="Encrypt",
                               variable=option,
                               value=1,
                               bg=self.background_color,
                               selectcolor=self.select_color,
                               fg=self.white,
                               font=("Arial",12)
                               )
    self.radioButton1.pack()

    self.radioButton2 = Radiobutton(self.frame,
                                    text="Decrypt",
                                    variable=option,
                                    value=2,
                                    bg=self.background_color,
                                    selectcolor=self.select_color,
                                    fg=self.white,
                                    font=("Arial",12)
                                    )
    self.radioButton2.pack()

    self.selectButton = Button(self.frame,
                               text="select",
                               bd=0,
                               fg=self.white,
                               bg=self.select_color,
                               font=("Arial",12),
                               command=lambda:self.selectButton_function(option.get())
                               )
    self.selectButton.pack()
    
  def run(self):
    self.window.mainloop()

    

  def selectButton_function(self,option):    
    if(self.last_option != option and not self.show_inputs):    
      self.show_inputs = True
      self.generateInputWigets()
      
    elif(self.last_option != option and self.show_inputs):
      self.destroyWidgets(self.label_priv_key,
                          self.label_public_key,
                          self.input_priv_key,
                          self.input_public_key,
                          self.encryptButton,
                          self.label_space)
      self.generateInputWigets()    
    
    if(option==1 and self.last_option != option):
      #Encrypt     
      self.setInputText(self.input_priv_key,"Hola")    
      self.encryptButton = Button(self.frame,
                                  height=1,
                                  text="Encrypt",
                                  bd=0,
                                  fg=self.white,
                                  bg=self.select_color,
                                  font=("Arial",12)
                                  )
      self.encryptButton.pack() 
         
    elif(option == 2 and self.last_option != option):
      #Decrypt    
      self.encryptButton = Button(self.frame,
                                  height=1,
                                  text="Decrypt",
                                  bd=0,
                                  fg=self.white,
                                  bg=self.select_color,
                                  font=("Arial",12)
                                  )
      self.encryptButton.pack()
    
    self.last_option = option
    
  def setInputText(self,input_entry,text):
    input_entry.delete(0,END)
    input_entry.insert(0,text)

  def destroyWidgets(self,*widgets):
    for i in widgets:
      i.destroy()
      
  def generateInputWigets(self,):
    
    self.label_priv_key = Label(self.frame,
                                text="Private Key:",
                                bg=self.background_color,
                                fg=self.white,
                                font=("Arial",12)
                                )
    self.label_priv_key.pack()
    self.input_priv_key = Entry(self.frame,text="")
    self.input_priv_key.pack()

    self.label_public_key = Label(self.frame,
                                  text="Public Key:",
                                  bg=self.background_color,
                                  fg=self.white,
                                  font=("Arial",12)
                                  )
    self.label_public_key.pack()
    self.input_public_key = Entry(self.frame,text="")
    self.input_public_key.pack() 
    self.label_space = Label(self.frame,
                             text="",
                             bg=self.background_color
                             )
    self.label_space.pack()

if __name__ == "__main__":
  gui = GUI()
  gui.run()