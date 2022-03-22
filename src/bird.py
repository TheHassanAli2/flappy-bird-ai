import pygame
import os

class Bird:
    ACCELERATION = 1 #Value for how fast the bird should accelerate downwards
    JUMP_CONST = -4.0 #Value for how much the bird should accelerate up by when it jumps
    TERMINAL_VELOCITY = 10.0 #Value for the amount of displacement where the bird stops accelerating
    
    def __init__(self, x, y, img = pygame.transform.scale(pygame.image.load(os.path.join("Assets","FBird_mediumwings.png")).convert_alpha(), (51, 36))):
        self.img = img
        self.x = x
        self.y = y
        self.height = self.y
        self.velocity = 0.0
        self.tick = 0
        self.rect = pygame.Rect(self.x, self.y, img.get_width(), img.get_height())
        self.failed = False
        
    #def update(self):

    def jump(self):
        self.velocity = self.JUMP_CONST
        self.tick = 0 #To restart the acceleration
        self.height = self.y
        
    def move(self):
        self.tick += 1
        #y = ax^2 + bx
        #d = vt + 0.5(at^2) kinematic equation, getting displacement of y for the movement of the bird
        displacement = self.velocity*(self.tick/2) + (0.5)*(self.ACCELERATION)*(self.tick/2)**2

        if displacement >= self.TERMINAL_VELOCITY:
            displacement = self.TERMINAL_VELOCITY if displacement > 0 else (-1)*(self.TERMINAL_VELOCITY) #Stays at T.V with the correct direction

        if displacement < 0:
            displacement -= 2 #If it jumped, make the acceleration upwards slowly turn downwards

        if self.y > 700:
            displacement = 0

        self.y = self.y + displacement
        self.rect.y = self.y
    def draw(self, window):
        window.blit(self.img, (self.rect.x, self.rect.y))
    def stop(self):
        self.JUMP_CONST = 0
    def start(self):
        self.JUMP_CONST = -10.0
