import pygame, sys, os, config
from pygame.constants import K_BACKSPACE, K_DOWN, K_RETURN, K_SPACE, KEYDOWN, MOUSEBUTTONDOWN, MOUSEMOTION  
from monika_animate import *
from pygame import mixer
from button import *
from music import *
from config import *
from chat import *
from Sprites_Load.monika_sprites import *
input_box1 = InputBox(245, 645, 140, 32)
input_boxes = [input_box1]

class GameState():                                          #different stages/background of game
    def __init__(self):
        self.state = 'background1'
    def background1(self):                                  # BACKGROUND 1
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:              
                if next_music_button.isOver(pos):
                    music.next()                            # Pause/Play     
                if pause_music_button.isOver(pos):
                    music.pause_or_play()                  
                if volume_up_button.isOver(pos):
                    music.volume_up()              
                if volume_down_button.isOver(pos):
                    music.volume_down()            
                if background2_button.isOver(pos):
                    music.hej_monika()
                    self.state = 'background2'              
                if chat_button.isOver(pos):
                    self.state = 'background4'
            if event.type == MOUSEMOTION:
                button_color_change()
               
        monika_animation()
        date_and_time()
        music_controls() 
        background2_button.draw(screen, (255, 255, 255))
        chat_button.draw(screen, (0, 0, 0))
        pygame.display.update()
    
    def background2(self):                            # BACKGROUND 2
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()    
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if background1_button.isOver(pos):
                    self.state = 'background1'
                    music.reset()
                if dark_button.isOver(pos):
                    self.state = 'background3'
                    pygame.mixer.music.unload()
                    mixer.music.load(os.path.join('Audios', "hej_monika_dark.ogg"))
                    mixer.music.set_volume(final_volume)
                    mixer.music.play()
            if event.type == MOUSEMOTION:
                if dark_button.isOver(pos):
                    dark_button.color = (200, 0, 0)
                    dark_button.text = "don't do it."
                else:   
                    dark_button.color = (255, 0, 0)
                    dark_button.text = "???"
                if background1_button.isOver(pos):
                    background1_button.color = (135, 82, 30)
                else:
                    background1_button.color = (188, 114, 49)
        monika_animation2()
        background1_button.draw(screen, (255, 255, 255))
        dark_button.draw(screen, (0, 0, 0))
        pygame.display.update()
    def background3(self):                             # BACKGROUND 3
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos() 
            if event.type == pygame.QUIT:
                pygame.quit()    
                sys.exit()
        monika_animation_half()
        pygame.display.update()
    def background4(self):  
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()    
                sys.exit()
            if event.type == MOUSEMOTION:
                button_color_change()
            if event.type == MOUSEBUTTONDOWN:
                if background1_button.isOver(pos):
                    self.state = 'background1'         
                if next_music_button.isOver(pos):
                    music.next()                            # Pause/Play     
                if pause_music_button.isOver(pos):
                    music.pause_or_play()                  
                if volume_up_button.isOver(pos):
                    music.volume_up()              
                if volume_down_button.isOver(pos):
                    music.volume_down() 
            for box in input_boxes:
                box.handle_event(event)   
        for box in input_boxes:
            box.update()
            box.resposne()
        for box in input_boxes:
            box.draw(screen)
        pygame.display.update()












    def state_manager(self):
        if self.state == 'background1':
            self.background1()
        if self.state == 'background2':
            self.background2()
        if self.state == 'background3':
            self.background3()
        if self.state == 'background4':
            self.background4()
game_state = GameState()