import pygame

class Button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 25)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width: #pos takes in 2 parameter, pos[0] gets 'x' of pos while pos[1] gets 'y' of pos
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
    def motion_color_change(self):
        pos = pygame.mouse.get_pos()
        if self.isOver(pos):
            self.color = (135, 82, 30)
        else:
            self.color = (188, 114, 49)

def button_color_change():
    next_music_button.motion_color_change()
    pause_music_button.motion_color_change()
    volume_up_button.motion_color_change()
    volume_down_button.motion_color_change()
    background1_button.motion_color_change()
    background2_button.motion_color_change()
    chat_button.motion_color_change()

    
next_music_button = Button((188, 114, 49), 1140, 75, 100, 25, 'next')
pause_music_button = Button((188, 114, 49), 990, 75, 135, 25, 'play/pause')
volume_up_button = Button((188, 114, 49), 1200, 400, 55, 25, 'up')
volume_down_button = Button((188, 114, 49), 1200, 515, 55, 25, 'down')
background2_button = Button((188, 114, 49), 935, 535, 160, 40, 'Hey Monika!!!')
background1_button = Button((188, 114, 49), 1100, 650, 160, 40, 'Return')
dark_button = Button((255, 0, 0), 1140, 15, 130, 40, '???')
chat_button = Button((188, 114, 49), 10, 400, 55, 25, 'Chat')
