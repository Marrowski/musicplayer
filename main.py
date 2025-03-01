import pygame
from pygame import mixer
from tkinter import *
from tkinter import ttk
import os


sound_pause = False
sound = None


def play():
    global sound, sound_pause
    pygame.mixer.init()
    sound = pygame.mixer.Sound('music/Виктор Цой - Группа крови.mp3')
    
    
    if sound_pause:
        pygame.mixer.unpause()
        sound_pause = False
    else:
        sound.play()
       
    
def pause():
    global sound_pause  
    if sound:
        pygame.mixer.pause()
        sound_pause = True
    
    
    
def stop():
    sound_stop = pygame.mixer.stop()
    

root = Tk()
root.geometry('1000x500')
root.title('Музичний плеєр')

btn_play = ttk.Button(text='▶️', command=play)
btn_pause = ttk.Button(text='⏸', command=pause)
btn_stop = ttk.Button(text='⏹', command=stop)

btn_play.pack()
btn_pause.pack()
btn_stop.pack()


root.mainloop()