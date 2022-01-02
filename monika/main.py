import pygame
from monika_animate import *
from button import *
from music import *
from config import *
from game_manager import *
pygame.init()
clock = pygame.time.Clock()
def main():                                # MAIN GAME LOOP
    while True:
        game_state.state_manager()
        clock.tick(60)        
if __name__ == "__main__":
    main()
    