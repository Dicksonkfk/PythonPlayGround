import pygame, os

#Farming area
MAIN_MENU_IMAGE = 'Main Menu'
CURRENT_TIME = 'current time'
LEVEL = 'level'
GRID_X_SIZE = 250
GRID_Y_SIZE = 350

#Screen Width
DISPLAY_H = 600
DISPLAY_W = 800

class Farm():


    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.drawText('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.screen.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.resetKeys()


class FarmMenu(Farm):
    def __init__(self, game):
        Farm.__init__(self, game)
        #self.farmx, self.farmy =  pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        #self.cursor_rect.midtop = (self.farmx + self.offset, self.farmy)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.checkEvents()
            self.game.check_input()

    def check_input(self, mapImg):
        if self.game.actions['start']:
            self.game.event_menu = self.game.farm
            self.grass_img = pygame.image.load(os.path.join(self.game.assets_dir, "map", "Components/grass.png"))
            #mapImg = pygame.image.load('Components/grass.png')
            #self.game.screen.blit(mapImg, (GRID_X_SIZE, GRID_Y_SIZE))
            #return mapImg
            pygame.display.update()


                #self.grass_img = pygame.image.load(os.path.join(self.game.assets_dir, "map", "Components/grass.png"))
