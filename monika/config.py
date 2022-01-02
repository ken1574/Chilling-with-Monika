import pygame, os
from datetime import datetime
pygame.font.init()

# colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Chilling with Monika :)')

plank = pygame.image.load(os.path.join('Images', 'plank.png')) 
plank = pygame.transform.scale(plank, (700, 75))
sign = pygame.image.load(os.path.join('Images', 'sign.png')) 
sign_rect = sign.get_rect()
sign = pygame.transform.scale(sign, (sign_rect.height//1.3, sign_rect.width//1.3))
monikastare = pygame.image.load(os.path.join('Images', 'monika_stare1.png')) 
monikastare = pygame.transform.scale(monikastare, (1280, 720))
pink_bar = pygame.image.load(os.path.join('Images', 'pink_bar.png'))

# FUNCTIONS

def date_and_time():
    now = datetime.now()
    now_date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    font = pygame.font.SysFont('comicsans', 25)
    text = font.render(f"{now_date_time}", True, (255, 255, 255))
    textRect = text.get_rect() #creates rectangular object for the text
    textRect.center = (125, 25)
    screen.blit(text, textRect) 

