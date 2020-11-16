# Pygame Tutorial Assignment
# Tutorial url: https://coderslegacy.com/python/python-pygame-tutorial/
# LAP WS 2020-2021, Week 3
# Group: AriaRay Brown, Ben Posner, Susann Boy

import pygame, sys
from pygame.locals import *
import random

# Initialize program
pygame.init()

"""
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
"""


# set fps
FPS = 60
FramePerSec = pygame.time.Clock()

# create colours
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# other variables that we will use
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

#display settings
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("GAME")

# create an enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png") #enemy sprite
        self.surf = pygame.Surface((50, 80)) #create rectangle for enemy sprite, size 50x80
        self.rect = self.surf.get_rect(center = (random.randint(40, 360), 0))   # enemy appears somewhere at the top
                                                                                # of the screen

    def move(self):
        # enemy moves downwards until it reaches the end of the screen, then appears again at top
        self.rect.move_ip(0, 10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect) # draw image on the rectangle; surface.blit(self.surf, self.rect) draws
                                            # a rectangle on a surface

# create player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.Surface((50, 100))
        self.rect = self.surf.get_rect(center=(150, 500)) # the player appears at the bottom of the screen

    def update(self):
        # player is able to move by pressing left/right keys
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:              # to ensure that the player can't move off the screen
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:  # to ensure that the player can't move off the screen
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

P1 = Player()
E1 = Enemy()

# start game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    P1.update()
    E1.move()

    DISPLAYSURF.fill(WHITE)
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)

    pygame.display.update()
    FramePerSec.tick(FPS)