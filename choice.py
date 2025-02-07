import time
import pygame
from settings import *
from sprite import Button

TITLE  = "Choice"
class choiceWindow:
    def __init__(self):
        self.end = False
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.startTime = time.time()
        self.puzzle_size = 0

    def new(self):
        self.buttons_list = []
        self.buttons_list.append(Button(300, 100, 300, 100, "2X2 Puzzle", WHITE, BLACK))
        self.buttons_list.append(Button(300, 400, 300, 100, "6X6 Puzzle", WHITE, BLACK))
        self.screen.fill(BGCOLOUR)
        for i in self.buttons_list:
            i.draw(self.screen)
        pygame.display.flip()
        
    def run(self):
        while not self.end:
            self.events()
        self.endTime = time.time()
        return self.puzzle_size

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for button in self.buttons_list:
                    if button.click(mouse_x, mouse_y):
                        if button.text == "2X2 Puzzle":
                            self.puzzle_size = 2
                            self.end = True
                        if button.text == "6X6 Puzzle":
                            self.puzzle_size = 6
                            self.end = True

    def timeTaken(self):
        return self.endTime - self.startTime
    

choice = choiceWindow()
while True:
    choice.new()
    c = choice.run()
    pygame.quit()
    print("choice: ",c)
    print("Time Taken:",choice.timeTaken())
    
    break            