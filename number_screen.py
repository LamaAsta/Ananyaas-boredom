import pygame
from settings import *
import random

class waitScreen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(title)    
        self.time = 2
        self.time *= 60
        self.screen.fill((255, 255, 255))  # Fill screen with white
        self.screen.blit()  # Draw at position (100,100)
        pygame.display.flip()
        self.font = pygame.font.Font(None, 36)

    def display_number(self):
        num = str(random.randint(0, 100))
        x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        text = self.font.render(num, True, WHITE)
        self.screen.blit(text, (x, y))

    def run(self):
        self.playing = True 
        while self.playing:
            self.display_number()
            pygame.display.flip()
            pygame.time.delay(1000)

a = waitScreen()
a.run()