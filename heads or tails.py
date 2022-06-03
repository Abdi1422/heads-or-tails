#heads or tails
import numpy as np
from tkinter import*
import random
from PIL import ImageTk,Image

def restart_program():
    label.grid_remove()
    label2.grid_remove()
    label3.grid(row=0,column=0)
           
def flip():
    label3.grid_remove()
    randy=random.randint(1,2)
    if randy==1:
        label.grid()
        label2.grid_remove()
    elif randy==2:
        label2.grid()
        label.grid_remove()
      
window=Tk()
window.title("heads or tails")
window.geometry("400x400")

coinbutton=Button(window,text="Flip",font=200,height=10,width=20,command= flip)
coinbutton.place(x=209,y=203)

refreshbutton=Button(window,text="restart",font=200,height=8,width=20,command= restart_program)
refreshbutton.place(x=209,y=40)

coin=Image.open("heads.png")
resized=coin.resize((205,225),Image.ANTIALIAS)
coin=ImageTk.PhotoImage(resized)
label=Label(window,padx=20,pady=20,image=coin)

coin2=Image.open("tails.png")
resized=coin2.resize((205,225),Image.ANTIALIAS)
coin2=ImageTk.PhotoImage(resized)
label2=Label(window,padx=20,pady=20,image=coin2)

label3=Label(window,text="Choose heads or tails." )
label3.grid(row=0,column=0)

window.mainloop()        
   