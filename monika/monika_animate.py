import pygame, getpass, sys
from Sprites_Load.monika_sprites import *
from config import *
pygame.init()

images = [monika1, monika2, monika3, monika4, monika5, monika6, monika7, monika8, monika9, monika10, monika11, monika12, monika13, monika14, monika15, monika16, monika17, monika16, monika15, monika14, monika13, monika12, monika11, monika10, monika9, monika8, monika7, monika6, monika5, monika4, monika3, monika2]
images2 = [monika1B, monika2B, monika3B, monika4B, monika5B, monika6B, monika7B, monika8B, monika7B, monika6B, monika5B, monika4B, monika3B, monika2B]
images3 = [group1, group2, group3, group4, group5]

counter = 0
nextdance = 0
wait = 0
wait2 = 0
def monika_animation():
    global counter
    if counter < 32:        
        screen.blit(images[int(counter)], (0, 0))
        counter += 0.2
        
    else:
        counter = 0
def monika_animation2():
    global counter, nextdance
    if nextdance < 100:
        if counter < 14:    
            screen.blit(images2[int(counter)], (0, 0))
            counter += 0.2  
            nextdance += 0.2 
        else:
            counter = 0
    elif nextdance > 100 and nextdance < 200:
        if counter < 5:    
            screen.blit(images3[int(counter)], (0, 0))
            counter += 0.2  
            nextdance += 0.2
        else:
            counter = 0
    elif nextdance > 200:
        nextdance = 0      
def monika_animation_half():
    global wait, counter, wait2
    username = getpass.getuser()
    if wait < 100:
        if counter < 14:
            screen.blit(images2[int(counter)], (0, 0))
            counter += 0.2  
            wait += 0.1
        else:
            counter = 0
    elif wait > 100:
        wait2 += 0.1
        if wait2 < 30:
            screen.blit(monikastare, (0, 0))
            font = pygame.font.SysFont('comicsans', 50)
            text = font.render(f"Hello there, {username}~", True, (255, 255, 255))
            screen.blit(text, text.get_rect(center = screen.get_rect().center))
        if wait2 > 30 and wait2 < 80:
            screen.blit(monikastare, (0, 0))
            font = pygame.font.SysFont('comicsans', 50)
            text = font.render(f"What brings you here?", True, (255, 255, 255))
            screen.blit(text, text.get_rect(center = screen.get_rect().center)) 
            wait2 += 0.1
        if wait2 > 80 and wait2 < 130:
            screen.blit(monikastare, (0, 0))
            font = pygame.font.SysFont('comicsans', 50)
            text = font.render(f"I'm afraid that you can't be here...", True, (255, 255, 255))
            screen.blit(text, text.get_rect(center = screen.get_rect().center)) 
            wait2 += 0.1
        if wait2 > 130 and wait2 < 160:
            screen.blit(monikastare, (0, 0))
            font = pygame.font.SysFont('comicsans', 50)
            text = font.render(f"See you later!", True, (255, 255, 255))
            screen.blit(text, text.get_rect(center = screen.get_rect().center)) 
            wait2 += 0.1
        if wait2 > 160:
            pygame.quit()
            sys.exit()
            