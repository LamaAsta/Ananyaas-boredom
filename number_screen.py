import pygame
import random
from settings import *
TITLE = "Wait Screen"

class WaitScreen:
    def __init__(self,n=2):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)    
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 50)
        self.n = n*10

    def display_number(self):
        num = str(random.randint(0, 100))
        x, y = random.randint(0, WIDTH - 50), random.randint(0, HEIGHT - 50)
        text = self.font.render(num, True, BLACK)
        self.screen.blit(text, (x, y))

    def run(self):
        running = True
        while running:
            if not self.n:
                running = False
            self.n -= 1
            self.screen.fill(WHITE) 
            self.display_number()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()
            pygame.time.delay(1000)  

# if __name__ == "__main__":
#     a = WaitScreen(1)
#     a.run()