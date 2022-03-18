import random
import pygame
import os

class Pipes:
    VELOCITY = 16.0 #The amount of pixels the pipes will be moving at
    GAP = 200 #The amount of pixels between the top and bottom pipe
    
    def __init__(self, x, img = pygame.transform.scale(pygame.image.load(os.path.join("Assets","pipe.png")).convert_alpha(), (104, 640))):
        self.bot_img = img
        self.top_img = pygame.transform.flip(img, False, True) #flipped the bottom pipe's image
        self.x = x
        self.randtick = 0
        self.randomHeight()
        self.rectbot = pygame.Rect(self.x, self.ybot, img.get_width(), img.get_height()) #Create a hitbox for the bottom pipe
        self.recttop = pygame.Rect(self.x, self.ytop, img.get_width(), img.get_height()) #Create a hitbox for the top pipe
        
    #def update(self):
    
    def randomHeight(self):
        random.seed(self.randtick)
        print(self.randtick)
        self.ybot = random.randint(200, 750) #Random Y value for the bot pipe
        self.ytop = self.ybot - (self.GAP + 640) #Y value for the top pipe

    def move(self):
        self.randtick+=1
        self.x -= self.VELOCITY
        self.rectbot.x = self.x
        self.recttop.x = self.x
        
        if self.x <-100:
            self.x += 700
            self.randomHeight()

    def draw(self, window):
        window.blit(self.bot_img, (self.rectbot.x, self.rectbot.y))
        window.blit(self.top_img, (self.recttop.x, self.recttop.y))

    