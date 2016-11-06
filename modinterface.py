import pygame, sys, time
from pygame.locals import *
import modcfg

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def splashPage(color):
    splashimg = pygame.image.load("spacealert.jpg")

    # draw the white background onto the surface
    windowSurface.fill(color)
    windowSurface.blit(splashimg,(200,100))
    pygame.display.update()


# Set events pour brasser la souris
#pygame.time.set_timer(USEREVENT+1,modcfg.perturn*1000)
#windowSurface = pygame.display.set_mode((1280, 960), pygame.FULLSCREEN)
windowSurface = pygame.display.set_mode((1024, 736), pygame.RESIZABLE)
## set up fonts
#basicFont = pygame.font.SysFont('droidsans', 48)
## set up the text
#text = basicFont.render('Space Alert!', True, WHITE, BLUE)
#pygame.display.set_caption('Hello world!')

## draw the text's background rectangle onto the surface
#textRect = text.get_rect()
#textRect.centerx = windowSurface.get_rect().centerx
#textRect.centery = windowSurface.get_rect().centery
#pygame.draw.rect(windowSurface, BLUE, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

## draw the text onto the surface
#windowSurface.blit(text, textRect)

## draw the window onto the screen
pygame.display.update()
