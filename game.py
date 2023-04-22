import pygame as pg
from menu import *
from farm import FarmMenu
import time

class Game():
    def __init__(self):
        #Initializing Pygame
        pg.init()
        self.running, self.playing = True, True
        self.actions = {"up": False, "down": False, "start": False, "back": False}

        #Create the output screen
        #self.screen = pg.display.set_mode((800,600))

        # Title and Icon
        pg.display.set_caption(" Simulation of Agriculture Farming Process")
        icon = pg.image.load('Components/menuIcon.png')
        pg.display.set_icon(icon)

        #Create classic font for menu
        self.font_name = 'Fonts/8-BIT WONDER.TTF'
        #self.font_name = pg.font.get.default_font()

        # RGB
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)

        #Screen Width
        self.DISPLAY_H = 600
        self.DISPLAY_W = 800
        self.display = pg.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.screen = pg.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.farm = FarmMenu(self)
        self.curr_menu = self.main_menu
        self.event_menu = self.farm

    def gameLoop(self):
        while self.playing:

            self.checkEvents()

    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def checkEvents(self):
            #Simulation Loop
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running, self.playing = False, False
                    self.curr_menu.run_display = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                       self.actions['start'] = True
                    if event.key == pg.K_BACKSPACE:
                        self.actions['back']= True
                    if event.key == pg.K_DOWN:
                        self.actions['down'] = True
                    if event.key == pg.K_UP:
                        self.actions['up'] = True

    def resetKeys(self):
        for action in self.actions:
            self.actions[action] = False

    def drawText(self, text, size, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def text_objects(self, text, color, size="small"):
        if size == "small":
            font = pygame.font.Font(self.font_name, 20)
            textSurface = font.render(text, True, color)
            # smallfont = pygame.font.SysFont("Times New Roman", 20)
            # textSurface = smallfont.render(text, True, color)
            return textSurface, textSurface.get_rect()

    #def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small"):

        #textSurf, textRect = Game().text_objects(msg, color, size)
        #textRect.center((buttonx + (buttonwidth / 2)), buttony + (buttonheight / 2))
        #screen.blit(textSurf, textRect)


    def playBtn(text, x, y, width, height, inactive_color, active_color, action=None):
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # print(click)
        if x + width > cur[0] > x and y + height > cur[1] > y:
            pg.draw.rect(screen, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "play":
                pg.event_menu.display_menu()
        else:
            pg.draw.rect(screen, inactive_color, (x, y, width, height))
            #Game().text_to_button(text, black, x, y, width, height)

    pg.draw.rect(screen, (255, 0, 0), ((DISPLAY_W / 2) - 250, (DISPLAY_H / 2) - 150, 100, 50))
    playBtn("play", 150, 500, 100, 50, green, light_green, action="play")
    pg.display.update()








