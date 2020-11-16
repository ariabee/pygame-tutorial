# Pygame Tutorial Assignment
# Tutorial url: https://coderslegacy.com/python/python-pygame-tutorial/
# LAP WS 2020-2021, Week 3
# Group: AriaRay Brown, Ben Posner, Susann Boy

import pygame, sys
from pygame.locals import *
import random

# Initialize program
pygame.init()

# Create color objects
BLACK = pygame.Color(0, 0, 0)       # Black
WHITE = pygame.Color(255, 255, 255) # White
GREY = pygame.Color(128, 128, 128)  # Grey
RED = pygame.Color(255, 0, 0)       # Red
BLUE  = (0, 0, 255)                 # Blue - "pygame.Color" is redundant?
GREEN = (175, 237, 161)             # Green

# Choose frames per second
FPS = 60 # aim for a value between 30-60
clock_object = pygame.time.Clock()

# Setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((300,300))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Example")

# Create lines and shapes on display
# Note: pygame.draw.rect() takes a tuple of 4 values
#     ( x-coordinate of upper left corner of rectangle,
#       y-coordinate of upper left corner of rectangle,
#       width of rectangle in pixels,
#       height of rectangle in pixels )
pygame.draw.line(DISPLAYSURF, BLUE, (150,130), (130,170))
pygame.draw.line(DISPLAYSURF, BLUE, (150,130), (170,170))
pygame.draw.line(DISPLAYSURF, GREEN, (130,170), (170,170))
pygame.draw.circle(DISPLAYSURF, GREEN, (100,50), 30)
pygame.draw.circle(DISPLAYSURF, BLACK, (200,50), 30)
pygame.draw.rect(DISPLAYSURF, RED, (100, 200, 100, 50), 2)
pygame.draw.rect(DISPLAYSURF, GREEN, (110, 260, 80, 20), 0)

# Game loop begins
while True:
      # Code
      # Code
      #.
      #.
      pygame.display.update()
      for event in pygame.event.get():
            if event.type == QUIT:
                  pygame.quit()
                  sys.exit()

      clock_object.tick(FPS) # game loop will execute this many FPS
