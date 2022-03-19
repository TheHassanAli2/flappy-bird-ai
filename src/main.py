from turtle import bgpic
import pygame
import os

pygame.init()

SCREEN_HEIGHT = 800  # mobile height for 8bit games
SCREEN_WIDTH = 600  # mobile width for 8 bit games

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird AI")
from bird import Bird #scaling of the bird image has to be done after the display function
from pipes import Pipes #Same as above

BG =  pygame.transform.scale(pygame.image.load(os.path.join("Assets","bgday.png")).convert_alpha(), (600, 900))

birds = [Bird(60,60)]
opipes = Pipes(600)

def gameOver():
    #pygame.quit()
    SCREEN.blit(BG, (0,0))

#Super ugly, will clean up
def hasCollided(bird, pipes):
    if (pipes.x <= bird.x or pipes.x <= (bird.x+51)) and (bird.x <= (pipes.x + 104) or (bird.x+51) <= (pipes.x + 104)): #If the bird is within the width of the pipe
        if (pipes.ytop <=  bird.y or pipes.ytop <=  (bird.y + 36)) and (bird.y <= (pipes.ytop + 640) or (bird.y + 36) <= (pipes.ytop + 640)):
            return True
        if (pipes.ybot <=  bird.y or pipes.ybot <=  (bird.y + 36)) and (bird.y <= (pipes.ybot + 640) or (bird.y + 36) <= (pipes.ybot + 640)):
            return True
        return False

def main():
    #pygame.mixer.music.load("../audio/music_zapsplat_easy_cheesy.mp3")
    # pygame.mixer.music.play(-1)
    # pygame.mixer.music.set_volume(0.2)
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if running == False:
                pygame.quit()
        
        SCREEN.blit(BG, (0,0))
        for bird in birds:
            bird.move()
            bird.draw(SCREEN)

        opipes.move()
        opipes.draw(SCREEN)
        user_input = pygame.key.get_pressed()

        for i, bird in enumerate(birds):
            if user_input[pygame.K_SPACE]:
                bird.jump()
        if hasCollided(bird, opipes):
            gameOver()
        pygame.display.update()
    pygame.quit()  # make sure this stays at the end of our file


main()
#
# i am halping
#
