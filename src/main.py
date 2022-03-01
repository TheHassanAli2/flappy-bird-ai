import pygame
import os

pygame.init()

SCREEN_HEIGHT = 1536  # mobile height for 8bit games
SCREEN_WIDTH = 864  # mobile width for 8 bit games
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird AI")


FLYING = pygame.image.load("../assets/FBird_mediumwings.png")


def main():
    pygame.mixer.music.load("../audio/music_zapsplat_easy_cheesy.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if running == False:
                pygame.quit()
            pygame.time.Clock()

    pygame.quit()  # make sure this stays at the end of our file


main()
#
#
#
