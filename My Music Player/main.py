import tkinter
import customtkinter
import pygame
from PIL import Image, ImageTk
from threading import *
import time
import math

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()

root.title('My Music Player')
root.geometry('400x480')
pygame.mixer.init()
root.configure(fg_color='#1a1c1f')

list_of_songs = ['music/Imagine Dragons - Believer.mp3','music/Imagine Dragons - Natural.mp3','music/Imagine Dragons - Whatever It Takes.mp3']
list_of_img = ['img/Beliver.jpg','img/Natural.jpg','img/Whatever It Takes.jpg']
s = 0

# Função para coleta do nome e da imagem da musica
def get_album_img(song_name, s):
    image1 = Image.open(list_of_img[s])
    image2 = image1.resize((250, 250))
    load = ImageTk.PhotoImage(image2)
    label1 = tkinter.Label(root, image=load)
    label1.image = load
    label1.place(relx=0.19, rely=0.06)

    stripped_string = song_name[6:-3]
    song_name_label = tkinter.Label(text= stripped_string, bg='#222222', fg='white')
    song_name_label.place(relx=0.3, rely=0.6)

#Barra de progresso de acordo com o tamanho da musica
def progress():
    a = pygame.mixer.Sound(f'{list_of_songs[s]}')
    song_leng = a.get_length() * 3
    for i in range(0, math.ceil(song_leng)):
        time.sleep(0.3)
        progressbar.set(pygame.mixer.music.get_pos() / 1000000)

def threading():
    t1 = Thread(target=progress)
    t1.start()

#Função que da o play na aplicação
def play_music():  
    threading()
    global s
    current_song = s
    if s > 2:
        s = 0
    song_name = list_of_songs[s]
    pygame.mixer.music.load(song_name)
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.5)
    get_album_img(song_name, s)
    s += 1

def skip_fordward():
    play_music()

def skip_back():
    global s
    s -= 2
    play_music()
    
def valume(value):
    pygame.mixer.music.set_volume(value)


#Bottuns

play_bottun = customtkinter.CTkButton(master=root, text='play', command=play_music)
play_bottun.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

skip_f = customtkinter.CTkButton(master=root, text='>', command=skip_fordward, width=2)
skip_f.place(relx=0.73, rely=0.7, anchor=tkinter.CENTER)

skip_b = customtkinter.CTkButton(master=root, text='<', command=skip_back, width=2)
skip_b.place(relx=0.27, rely=0.7, anchor=tkinter.CENTER)

slider = customtkinter.CTkSlider(master=root, from_= 0, to = 1, command=valume, width=210)
slider.place(relx=0.5, rely=0.78, anchor=tkinter.CENTER)

progressbar = customtkinter.CTkProgressBar(master=root, progress_color='#05ad17', fg_color = '#3e4145', border_width=0.1, width=250, height=2)
progressbar.place(relx=0.5, rely=0.85, anchor=tkinter.CENTER)

root.mainloop()

#My Music Player é um projeto de um player de musica feito em python utilizando bibliotecas como PyGame (mixer), CustomTkinter, Threading e PIL.
