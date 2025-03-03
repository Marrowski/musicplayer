import pygame
from pygame import mixer
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
import os


pygame.mixer.init()
sound_pause = False
sound_stop = False
file = None


def open_file():
    global file, sound_vol
    file = filedialog.askopenfile(mode='r')

def play():
    global sound_pause
    
    if file:
        if sound_pause:
            pygame.mixer.music.unpause()
            sound_pause = False
        else:
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
    else:
        label_file = ttk.Label(text='Будь ласка завантажте файл!')
        label_file.pack()
        
    
    
         
    
def pause():
    global sound_pause
    
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        sound_pause = True
    else:
        label_non_play = ttk.Label(text='Наразі нічого не програється.')
        label_non_play.pack()
    
    
    
def stop():
    pygame.mixer.music.stop()
    

def sound_vol(volume):
    mixer.music.set_volume(float(volume)/100)
    
    

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

scal = Scale(root,orient=HORIZONTAL ,length=300,from_=0,to=100 ,tickinterval=10,resolution=10, command=sound_vol)
scal.set(50)

scal.pack(side='left', padx=10)
scal.pack(side='right', padx=300)
scal.pack(side='bottom', pady=70)

button_file = Button(text='Вибрати файл', command=open_file)
button_file.pack()

root.configure(bg='DeepSkyBlue')
root.mainloop()