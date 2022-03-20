import random
import pygame
import time
import os

class Pipes:
    VELOCITY = 8.0 #The amount of pixels the pipes will be moving at
    GAP = 200 #The amount of pixels between the top and bottom pipe
    
    def __init__(self, x, img = pygame.transform.scale(pygame.image.load(os.path.join("Assets","pipe.png")).convert_alpha(), (104, 640))):
        self.bot_img = img
        self.top_img = pygame.transform.flip(img, False, True) #flipped the bottom pipe's image
        self.base_img = pygame.transform.scale(pygame.image.load(os.path.join("Assets","base.png")).convert_alpha(), (1700, 200))
        self.x = x
        self.countScore = True
        self.base_x = 0
        self.randomHeight()
        
    #def update(self):
    
    def randomHeight(self):
        self.ybot = random.randint(300, 650) #Random Y value for the bot pipe
        self.ytop = self.ybot - (self.GAP + 640) #Y value for the top pipe
        self.countScore = True

    def move(self):
        self.x -= self.VELOCITY
        self.base_x -= self.VELOCITY
        
        if self.x <-100:
            self.x += 700
            self.randomHeight()
        if self.base_x <-800:
            self.base_x += 723

    def draw(self, window):
        window.blit(self.bot_img, (self.x, self.ybot))
        window.blit(self.top_img, (self.x, self.ytop))
        window.blit(self.base_img, (self.base_x, 700))
    def stop(self):
        self.VELOCITY = 0
    def start(self):
        self.VELOCITY = 16.0

    