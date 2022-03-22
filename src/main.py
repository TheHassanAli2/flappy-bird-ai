import pygame
import os

pygame.init() #initialize pygame module

#global variables are capitalized in python
SCREEN_HEIGHT = 800  # mobile height for 8bit games
SCREEN_WIDTH = 600  # mobile width for 8 bit games

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird AI") #name of window popup

#need to import after creating screen, otherwise there is no screen variable being passed to the pipe and bird objects
from bird import Bird #scaling of the bird image has to be done after the display function
from pipes import Pipes #Same as above

#can also use night background
#convert alpha standardizes .png and .jpeg files
#scales image to screen resolution to avoid spill
BG =  pygame.transform.scale(pygame.image.load(os.path.join("Assets","bgday.png")).convert_alpha(), (600, 800))

#font for general text
FONT = pygame.font.SysFont("comicsans", 50)

birds = [Bird(160,300)] #object of Bird, passing in size | can add more to this list
pipe_object = Pipes(600) #x-coord of pipe, where it starts with y-coord being randomized
score = 0

def main():
    #TODO fix audio file or pick new one
    #pygame.mixer.music.load("../audio/music_zapsplat_easy_cheesy.mp3")
    # pygame.mixer.music.play(-1)
    # pygame.mixer.music.set_volume(0.2)
    clock = pygame.time.Clock()
    
    global score #this sets a global variable despite this otherwise being local to the main() functio
    score = 0
    running = True
    while running:
        clock.tick(60) #FPS affects everything's clock speed
        
        #displays background to screen based on (0, 0) coordinates with
        #the origin being in the top-left, as with all pygame programs
        SCREEN.blit(BG, (0,0))  

        #this enumerates each bird, giving them a number such as bird:1 and this
        #number is stored as i
        for i, bird in enumerate(birds):
            pipe_object.move() #moves to left
            pipe_object.draw(SCREEN)
            bird.move()
            bird.draw(SCREEN)
            
            #all events such as mouse movements and keyboard presses are included here
            for event in pygame.event.get():
                #simply controlling program flow with an ending clause
                if event.type == pygame.QUIT:
                    running = False
                if running == False:
                    pygame.quit()
                #tracks key presses
                if event.type == pygame.KEYDOWN:
                    #checks for jump and waits for it to 'come back up' to avoid spamming
                    #bird.failed checks if they've lost already by bumping the pipe
                    if event.key == pygame.K_SPACE and bird.failed == False: 
                        bird.jump()
            
            #TODO check if True parameter is for bolding of font
            text = FONT.render(f"{score}", True, (0,0,0))
            
            #coords of text
            SCREEN.blit(text,(275,100))
            
            hasCollided(bird, pipe_object)
            
            if(bird.failed):
                #making pipe and bird stop moving
                pipe_object.stop()
                bird.stop()
                gameOver()

            #updating display constantly
            pygame.display.update()
    pygame.quit()  # make sure this stays at the end of our file

def gameOver():
    #pygame.quit()
    text = FONT.render(f"dead", True, (0,0,0))
    SCREEN.blit(text,(275,100))

#Super ugly, will clean up
#simply checks if x or y values collide by checking between the pipe and bird objects
def hasCollided(bird, pipes):
    global score
    if (bird.y + 36) >= 700:
        bird.failed = True
    if (pipes.x <= bird.x or pipes.x <= (bird.x+51)) and (bird.x <= (pipes.x + 104) or (bird.x+51) <= (pipes.x + 104)): #If the bird is within the width of the pipe
        if (pipes.ytop <=  bird.y or pipes.ytop <=  (bird.y + 36)) and (bird.y <= (pipes.ytop + 640) or (bird.y + 36) <= (pipes.ytop + 640)):
            bird.failed = True
        elif (pipes.ybot <=  bird.y or pipes.ybot <=  (bird.y + 36)) and (bird.y <= (pipes.ybot + 640) or (bird.y + 36) <= (pipes.ybot + 640)):
            bird.failed = True
        elif (pipes.x<= 60 and pipes.countScore):
            pipes.countScore = False
            score+=1

main()
#
# i am halping
#
