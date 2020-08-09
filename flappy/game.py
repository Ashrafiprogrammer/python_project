import pygame
from pygame.locals import*
import sys
import random
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENWIDTH))
GROUNDY = SCREENHEIGHT*0.8
GAME_SPRITES = {}
GAME_SOUND = {}
PLAYER = 'gallery\sprites\bird.png'
BACKGROUND = 'gallery\sprites\background.png'
PIPE = 'gallery\sprites\pipe.png'


def welcomescreen():
    """
    shows welcome images on the screen

    """
    playerx = int(SCREENWIDTH/5)
    Playery = int((SCREENHEIGHT-GAME_SPRITES['player'].get_height())/2)
    messagex = int((SCREENWIDTH-GAME_SPRITES['message'].get_width())/2)
    messagey = int((SCREENHEIGHT*0.13))
    basex = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.QUIT()
                sys.exit()
            elif event.type == KEYDOWN and(event.key == K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                SCREEN.blit(GAME_SPRITES['player'], (playerx, Playery))
                SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey))
                SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)


def mainGame():
    score = 0
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENWIDTH/2)
    basex = 0
    newpipe1 = getRandompipe()
    newpipe2 = getRandompipe()
    upperpipe = [
        {'x': SCREENWIDTH+200, 'y': newpipe1[0]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y': newpipe2[0]['y']},

    ]
    lowerpipe = [
        {'x': SCREENWIDTH+200, 'y': newpipe1[1]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y': newpipe2[1]['y']},


    ]
    pipevl = 4
    playervl = -9
    playermx = 10
    playermi = -8
    playerac = 1
    playerFlapac = -8
    playerF = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playervl = playerac
                    playerF = True
                    GAME_SOUND['wing'].play()
        crashtest = isCollide(playerx, playery, upperpipe, lowerpipe)
        if crashtest:
            return