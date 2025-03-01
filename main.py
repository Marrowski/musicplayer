import pygame
from pygame import mixer
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
import os


sound_pause = False
sound = None
file = None


def open_file():
    global file
    file = filedialog.askopenfile(mode='r')

def play():
    global sound, sound_pause
    pygame.mixer.init()
    sound = pygame.mixer.Sound(file)
          
    if sound_pause:
        pygame.mixer.unpause()
        sound_pause = False
    else:
        sound.play()
        
    if sound is None:
        label_exc = tk.Label(root, textvariable=val, font=("Arial", 14))
        label_exc.pack()
    else:
        sound.play()
    
        
    
       
    
def pause():
    global sound_pause  
    if sound:
        pygame.mixer.pause()
        sound_pause = True
    
    
    
def stop():
    sound_stop = pygame.mixer.stop()
    

def sound_vol(val):
    mixer.music.set_volume(float(val)/10)
    

root = Tk()
root.geometry('900x400')
root.title('Музичний плеєр')

btn_play = ttk.Button(text='▶️', command=play)
btn_pause = ttk.Button(text='⏸', command=pause)
btn_stop = ttk.Button(text='⏹', command=stop)

label_main = ttk.Label(text='Музичний плеєр', font=('Arial', 22), background='DeepSkyBlue')
label_nick = ttk.Label(text='Розробник - Marrowski', font=('Arial', 22), background='DeepSkyBlue')

btn_play.place(relx=0.5, rely=0.5, anchor="c", width=80, height=40)
btn_pause.place(relx=0.4, rely=0.5, anchor="c", width=80, height=40)
btn_stop.place(relx=0.6, rely=0.5, anchor="c", width=80, height=40)

label_main.pack()
label_nick.pack()

scal = Scale(root,orient=HORIZONTAL ,length=300,from_=0,to=100,tickinterval=10,resolution=10, command=sound_vol)
scal.pack(side='left', padx=10)
scal.pack(side='right', padx=300)
scal.pack(side='bottom', pady=70)

button_file = Button(text='Вибрати файл', command=open_file)
button_file.pack()

val = tk.StringVar()
val.set('Спочатку виберіть файл!')
    

root.configure(bg='DeepSkyBlue')
root.mainloop()