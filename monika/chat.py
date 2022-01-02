import pygame, getpass
from config import *
from music import *
from Sprites_Load.monika_sprites import *
pygame.init()

COLOR_INACTIVE = pygame.Color('white')
FONT = pygame.font.Font(None, 32)
font = pygame.font.SysFont('comicsans', 50)
wait = 0

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.typed_text = text
        self.response = ''

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.typed_text = self.text
                self.text = ''
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        self.response_surface = font.render(self.response, True, self.color)
        screen.blit(self.response_surface, (245, 530)) 
        pygame.draw.rect(screen, self.color, self.rect, 2)

    def resposne(self):
        if self.typed_text == 'hi':
            global wait
            wait += 0.1
            if wait < 15:
                username = getpass.getuser()
                self.response = f"Hello {username}!"
                screen.blit(monika_talk, (0, 0))
                screen.blit(pink_bar,(720/2 - 125, 1280/2 - 100))
                music_controls()
                background1_button.draw(screen, (0, 0, 0))
            else:
                self.typed_text = ''
                self.response = ''
                wait = 0
                screen.blit(monika_idle, (0, 0))
                screen.blit(pink_bar,(720/2 - 125, 1280/2 - 100))
                music_controls()
                background1_button.draw(screen, (0, 0, 0))        
        else:
            screen.blit(monika_idle, (0, 0))
            screen.blit(pink_bar,(720/2 - 125, 1280/2 - 100))
            music_controls()
            background1_button.draw(screen, (0, 0, 0))      