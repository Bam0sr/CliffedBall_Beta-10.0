import pygame
import random
from Settings import *

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Cliffed Ball")
clock = pygame.time.Clock()

#Game Main Loop
running = True
while running:
    clock.tick(FPS)
    #process
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    #update
    #render
    screen.fill(BLACK)
    pygame.display.flip()
pygame.quit()



'''
import pygame
import random
from Sprites import *
from Settings import *

class Game:
    def __init__(self):
        #initialize
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption(TITILE)
        self.clock = pygame.time.Clock()
        self.running=True
    def new(self):
        #to create a new game
        self.all_sprites = pygame.sprites.Group()
        self.run()
    def run(self):
        #the loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        #game loop that updates
        pass
    def events (self):
        #game loop that event checks
        #process
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing=False
                running=False
    def draw(self):
        #drawing
        screen.fill(BLACK)
        pygame.display.flip()
    def show_menu(self):
        pass
    def show_game_over(self):
        pass

Mg= Game()
Mg.show_menu()
while Mg.running:
    Mg.new()
    Mg.show_game_over()


pygame.quit()
'''
