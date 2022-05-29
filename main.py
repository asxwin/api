from tkinter import *
from PIL import Image
from PIL import Image, ImageTk
from win32com.client import Dispatch
from time import sleep
from tkinter import ttk
import tkinter as tk
import os

root = Tk()
root.resizable(width=False, height=False)
root.title("DJ Khabi🦖")

frameCnt = 14
frames = [PhotoImage(file='api\disc.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]
playimg = ImageTk.PhotoImage(Image.open("api/pb.png"))
pauseimg = ImageTk.PhotoImage(Image.open("api/pause.png"))
previmg = ImageTk.PhotoImage(Image.open("api/next.png"))
nextimg = ImageTk.PhotoImage(Image.open("api/prev.png"))

muteimg1 = Image.open("api/mute.png")
muteimg2=muteimg1.resize((20,20), Image.ANTIALIAS)
muteimg=ImageTk.PhotoImage(muteimg2)

unmuteimg1 = Image.open("api/volume.png")
unmuteimg2=unmuteimg1.resize((20,20), Image.ANTIALIAS)
unmuteimg=ImageTk.PhotoImage(unmuteimg2)



mp = Dispatch("WMPlayer.OCX")

def play():
   
    for filename in os.listdir('api/songs'):
        if filename.endswith('.mp3'):
            tune = mp.newMedia('api/songs/'+filename)
            mp.currentPlaylist.appendItem(tune)
    mp.controls.play()
    mp.controls.playItem(tune)
    button2=ttk.Button(root,image=pauseimg,command=pause)
    button2.place(anchor=CENTER,x=498/2,y=473/2)
   
   
def playcont():
    mp.controls.play()
    button2=ttk.Button(root,image=pauseimg,command=pause)
    button2.place(anchor=CENTER,x=498/2,y=473/2)

def pause():
    mp.controls.pause()
    button1=ttk.Button(root,image=playimg,command=playcont)
    button1.place(anchor=CENTER,x=498/2,y=473/2)

def mute():
    mp.settings.Mute=True
    button3=Button(root,image=unmuteimg,command=unmute,height=20,width=20)
    button3.place(anchor=CENTER,x=498/2,y=673/2)   

def unmute():
    mp.settings.Mute=False
    button3=Button(root,image=muteimg,command=mute,height=20,width=20)
    button3.place(anchor=CENTER,x=498/2,y=673/2)

current_value = tk.DoubleVar()
def get_current_value():
    return '{: .2f}'.format(current_value.get())

def set_volume(event):
    mp.settings.volume=get_current_value()

def nexts():
    mp.controls.next()
def prevs():
    mp.controls.previous()

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)


label = Label(root)
label.pack()

button3=Button(root,image=muteimg,command=mute,height=20,width=20)
button3.place(anchor=CENTER,x=498/2,y=673/2)

button1=ttk.Button(root,image=playimg,command=play)
button1.place(anchor=CENTER,x=498/2,y=473/2)

nbutton1=ttk.Button(root,image=nextimg,command=nexts)
nbutton1.place(anchor=CENTER,x=298/2,y=473/2)
pbutton1=ttk.Button(root,image=previmg,command=prevs)
pbutton1.place(anchor=CENTER,x=698/2,y=473/2)


slider = ttk.Scale(root,from_=100,to=0,orient='vertical',variable=current_value,command=set_volume)
slider.set(100)


slider.place(anchor=CENTER,x=120/2,y=473/2)
root.iconbitmap(r'C:\Users\ashwi\OneDrive\Desktop\OS\api\icon.ico')

root.attributes('-alpha',0.5)
root.after(0, update, 0)

root.mainloop()