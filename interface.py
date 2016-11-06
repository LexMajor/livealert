import pygame, sys, time
import socket, os, os.path
import time
from pygame.locals import *

# set up pygame
pygame.init()


# Only a test
# set up the window
#screen = pygame.display.get_surface()
#w,h = screen.get_width(),screen.get_height()
#flags = screen.get_flags()
#jbits = screen.get_bitsize()
#screen = pygame.display.set_mode((w,h),flags^FULLSCREEN,bits)
#windowSurface = pygame.display.set_mode((500, 400), 0, 32)
windowSurface = pygame.display.set_mode((1024, 736), pygame.FULLSCREEN)
pygame.display.set_caption('Hello world!')

splashimg = pygame.image.load("spacealert.jpg")

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

altern = True

# set up fonts
#basicFont = pygame.font.SysFont(None, 48)
basicFont = pygame.font.SysFont('droidsans', 48)

# set up the text
text = basicFont.render('Space Alert!', True, WHITE, BLUE)

# draw the white background onto the surface
windowSurface.fill(WHITE)
windowSurface.blit(splashimg,(0,0))

# 
#pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

# draw a red ellipse onto the surface
#pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

# draw the text's background rectangle onto the surface
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery
pygame.draw.rect(windowSurface, BLUE, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# draw the text onto the surface
windowSurface.blit(text, textRect)

# draw the window onto the screen
pygame.display.update()

# Open Socket 
if os.path.exists( "/tmp/socket_interface" ):
  os.remove( "/tmp/socket_interface" )
 
print "Opening socket..."
server = socket.socket( socket.AF_UNIX, socket.SOCK_DGRAM )
server.bind("/tmp/socket_interface")


# run the game loop
while True:

    while True:
      datagram = server.recv( 1024 )
      if not datagram:
        break
      else:
        if (altern==True):
            pygame.draw.rect(windowSurface, (255,0,0), (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))
            altern=False
        elif (altern==False):
            pygame.draw.rect(windowSurface, (0,255,0), (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))
            altern=True
        windowSurface.blit(text, textRect)
        pygame.display.update()
        print "-" * 20

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

