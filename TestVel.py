import pygame
import random
from Settings import *
vec = pygame.math.Vector2

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
ball = pygame.image.load('18210-ball 2.png')
#ball = pygame.transform.scale(ball, (110, 100))

'''
BallPos = vec(150,150)
BallVel = vec(0,0)
BallAcc = vec(0,0)
'''

pos=[150,150]
x_change = 0
#Game Main Loop
running = True
def drawBall(x,y):
    screen.blit(ball,(x,y))

while running:
    clock.tick(FPS)
    #process
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_change = -5
    if keys[pygame.K_RIGHT]:
        x_change = 5
    #    if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
    #        BallAcc.x = 0
    if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        x_change = 0

    #update
    pos[0]+=x_change
    '''
    if BallPos.x > WIDTH:
        BallPos.x = -141
    if BallPos.x < -141:
        BallPos.x = WIDTH
    if BallPos.y == 119:
        BallVel.y = 0
    '''
    #render

    screen.fill(BLACK)
    drawBall(pos[0],pos[1])
    pygame.display.flip()
pygame.quit()
