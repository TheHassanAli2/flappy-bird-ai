import pygame
import os
import neat
import math

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


score = 0

def remove(index):
    birds.pop(index)
    ge.pop(index)
    nets.pop(index)

def eval_genomes(genomes, config):
    
    #TODO fix audio file or pick new one
    #pygame.mixer.music.load("../audio/music_zapsplat_easy_cheesy.mp3")
    # pygame.mixer.music.play(-1)
    # pygame.mixer.music.set_volume(0.2)
    clock = pygame.time.Clock()
    
    global score, birds, nets, pipe_object, ge #this sets a global variable despite this otherwise being local to the main() functio
    score = 0
    running = True
    birds = [] #object of Bird, passing in size | can add more to this list
    ge = [] #info on each individual bird for the algorithm
    nets = []
    pipe_object = Pipes(600) #x-coord of pipe, where it starts with y-coord being randomized

    for genome_id, genome in genomes: #for each of the 15 birds created
        birds.append(Bird(160,300))  #create a bird object
        ge.append(genome)  #Add the bird genome to the genome list
        net = neat.nn.FeedForwardNetwork.create(genome, config) #create a neural network of inputs and outputs for each genome
        nets.append(net) #Add each neural network to the nets list
        genome.fitness = 0 #Every genome starts with a fitness level of 0

    

    while running:
        clock.tick(60) #FPS affects everything's clock speed
        
        #displays background to screen based on (0, 0) coordinates with
        #the origin being in the top-left, as with all pygame programs
        SCREEN.blit(BG, (0,0))  

        #this enumerates each bird, giving them a number such as bird:1 and this
        #number is stored as i
        pipe_object.move() #moves to left
        pipe_object.draw(SCREEN)
        for i, bird in enumerate(birds):
            
            bird.move()
            bird.draw(SCREEN)

            x_dist = pipe_object.x - bird.x #Distance between bird and pipes for the neural network
            y_dist = bird.y - pipe_object.ybot #Distance between bird and pipes for the neural network
            
            output = nets[i].activate((bird.y, x_dist, y_dist)) #Output of 
            if output[0] > 0.5:
                press_space = pygame.event.Event(pygame.KEYDOWN, unicode=" s", key=pygame.K_SPACE, mod=pygame.KMOD_NONE) #simulate a space press
                pygame.event.post(press_space) #add the event to the queue
            
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
                # pipe_object.stop()
                ge[i].fitness -=1
                remove(i)
                 #When a dinosaur collides, they will be considered less fit and thus won't pass their genes
                # gameOver()

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

def run(config_path): #Setting up the neat algorithm
    config = neat.config.Config( #setting default parameters
        neat.DefaultGenome, 
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path #giving the config path for the neat algorithm
    )

    pop = neat.Population(config)
    pop.run(eval_genomes,50)

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir,'config.txt')
    run(config_path)
#
# i am halping
#
