import pygame as py
import pygame.time

import piano_keys_list as pl
from pygame import mixer

py.init()
mixer.init()

timer=pygame.time.Clock()
fps=60

font = pygame.font.Font('Terserah.ttf', 48)
medium_font = pygame.font.Font('Terserah.ttf', 28)
white_key_font = pygame.font.Font('Terserah.ttf', 24)
black_key_font=pygame.font.Font('Terserah.ttf',18)
real_small_font = pygame.font.Font('Terserah.ttf', 10)

screen = py.display.set_mode((1375,700))
icon=py.image.load('logo.png')
py.display.set_icon(icon)
py.display.set_caption('My Music Keybord')



def draw_keys():
    white_keys=[]
    black_keys=[]
    for i in range(14):
        rec=py.draw.rect(screen,'white',[i*98.21,400,95,300],0,2)
        white_keys.append(rec)
        key_label = white_key_font.render(pl.white_notes[i], True, 'black')
        screen.blit(key_label, (i * 98.21 + 40, 650))
    for i in pl.black_pos:
        rec=py.draw.rect(screen,'black',[i+60,400,45,200],0,2)
        black_keys.append(rec)
        key_label=black_key_font.render(pl.black_notes[pl.black_pos.index(i)],True,'white')
        screen.blit(key_label,(i+65,550))

def play_sound(x):
    if x in pl.ranges(start):
        play_note = py.mixer.Sound(x+'.wav')
        play_note.play()

start=0
active=1
while active:
    timer.tick(fps)
    draw_keys()
    for event in py.event.get():
        if event.type==py.QUIT:
            active=0
        if event.type ==py.KEYUP:
            input_event=chr(event.key).upper()
            play_sound(pl.search(input_event, start))

    py.display.flip()
