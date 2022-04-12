import random
import pygame
import os

class Pipes:
    VELOCITY = 0.333 #The amount of pixels the pipes will be moving at per tick
    
    #TODO as score increases, this should be decreased to make the game more difficult
    #? could be linear or reciprocal to a certain point
    GAP = 200 #The amount of pixels between the top and bottom pipe
    
    def __init__(self, x, img = pygame.transform.scale(pygame.image.load(os.path.join("Assets","pipe.png")).convert_alpha(), (104, 640))):
        self.bot_img = img
        self.top_img = pygame.transform.flip(img, False, True) #flipped the bottom pipe's image

        #stretch base of image to avoid it cutting into screen so that when it moves, the right part of it doesn't disappear to keep this 
        #animation looping
        self.base_img = pygame.transform.scale(pygame.image.load(os.path.join("Assets","base.png")).convert_alpha(), (1700, 200))
        
        self.x = x
        self.countScore = True
        self.base_x = 0
        self.randomHeight()
        
    #def update(self):
    
    #creates new pipes with random height
    def randomHeight(self):
        self.ybot = random.randint(300, 650) #Random Y value for the bot pipe

        #since origin of coordinates in pygame start at the top left, the y value increases as you go down
        #rather than the conventional increase going upwards
        #adding 640 to move image up (as it's really being subtracted)
        self.ytop = self.ybot - (self.GAP+640) #Y value for the top pipe 
        self.countScore = True #this variable's purpose is to cap score for 1 per pipe gap

    def move(self):
        #these start at different places so simply using the same variable won't work despite same velocity
        self.x -= self.VELOCITY
        self.base_x -= self.VELOCITY
        
        #off screen
        if self.x <-100:
            self.x += 700 #goes to right of screen again
            self.randomHeight() #next pipe will have another random height, this generates that
        if self.base_x <-800:
            self.base_x += 723

    #take in screen, display bottom image, top image with their respective x, y values
    def draw(self, window):
        window.blit(self.bot_img, (self.x, self.ybot))
        window.blit(self.top_img, (self.x, self.ytop))
        window.blit(self.base_img, (self.base_x, 700))
    def stop(self):
        self.VELOCITY = 0
    def start(self):
        #useful for when restart of game to move pipes again
        self.VELOCITY = 16.0