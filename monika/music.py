import pygame, os, random
from pygame import mixer
from pygame.constants import MOUSEBUTTONDOWN, MOUSEMOTION 
from button import * 
from config import *
current_music = ['Your_Reality', 'Your_Reality_Remix', 'Heat_Waves', 'Fukashigi_no_Carte_Remix', 'Racing_Into_The_Night']

final_volume = 0.2
queue = 0
paused = False
mixer.init()
mixer.music.load(os.path.join('Audios', f"{current_music[queue]}.ogg"))
mixer.music.set_volume(final_volume)
mixer.music.play(loops = -1)


def now_playing():
    font = pygame.font.SysFont('comicsans', 25)
    text = font.render(f"Now playing: {current_music[queue]}...", True, (255, 255, 255))
    textRect = text.get_rect() #creates rectangular object for the text
    textRect.center = (900, 35)
    screen.blit(plank, (595, 0))
    screen.blit(text, textRect) 

def volume_display():
    font = pygame.font.SysFont('comicsans', 40)
    rounded_volume = "{:.1f}".format(final_volume)  
    text = font.render(f"Vol: {rounded_volume}", True, (255, 255, 255))
    screen.blit(sign, (840, 355))
    screen.blit(text, (920, 435)) 


class Music:
    def next(self):
        global queue
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        queue = queue + 1
        if queue < len(current_music):
            mixer.music.load(os.path.join('Audios', f"{current_music[queue]}.ogg"))
            mixer.music.set_volume(final_volume)
            mixer.music.play(loops = -1)
        else:
            queue = 0
            mixer.music.load(os.path.join('Audios', f"{current_music[queue]}.ogg"))
            mixer.music.set_volume(final_volume)
            mixer.music.play(loops = -1)
    def pause_or_play(self):
        global paused
        if paused == False:
            pygame.mixer.music.pause()
            paused = True
        elif paused == True:
            pygame.mixer.music.unpause()
            paused = False
    def volume_up(self):
        global final_volume
        final_volume = final_volume + 0.1
        pygame.mixer.music.set_volume((final_volume))
    def volume_down(self):
        global final_volume
        if final_volume > 0:
            final_volume = final_volume - 0.1
            pygame.mixer.music.set_volume((final_volume))
        else:
            pygame.mixer.music.set_volume(0)
    def hej_monika(self):
        global final_volume
        pygame.mixer.music.unload()
        mixer.music.load(os.path.join('Audios', "hej_monika.ogg"))
        mixer.music.set_volume(final_volume)
        mixer.music.play(loops = -1)
    def reset(self):
        pygame.mixer.music.unload()
        mixer.music.load(os.path.join('Audios', f"{current_music[queue]}.ogg"))
        mixer.music.set_volume(final_volume)
        mixer.music.play(loops = -1)
music = Music()

def music_controls():
    now_playing()
    volume_display()
    next_music_button.draw(screen, (0, 0, 0))
    pause_music_button.draw(screen, (0, 0, 0))
    volume_up_button.draw(screen, (0, 0, 0))
    volume_down_button.draw(screen, (0, 0, 0))