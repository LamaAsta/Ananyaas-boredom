import time
import pygame
from settings import *
from sprite import Button,InputBox

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
        self.buttons_list.append(Button(200+200-70, 100, 300, 100, "4 Piece Puzzle", WHITE, BLACK))
        self.buttons_list.append(Button(200+200-70, 300, 300, 100, "9 Piece Puzzle", WHITE, BLACK))
        self.buttons_list.append(Button(200+540-70, 100, 300, 100, "16 Piece Puzzle", WHITE, BLACK))
        self.buttons_list.append(Button(200+540-70, 300, 300, 100, "25 Piece Puzzle", WHITE, BLACK))
        self.buttons_list.append(Button(230+340-70, 500, 300, 100, "36 Piece Puzzle", WHITE, BLACK))
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
                        if button.text == "4 Piece Puzzle":
                            self.puzzle_size = 2
                            self.end = True
                        if button.text == "9 Piece Puzzle":
                            self.puzzle_size = 3
                            self.end = True
                        if button.text == "16 Piece Puzzle":
                            self.puzzle_size = 4
                            self.end = True
                        if button.text == "25 Piece Puzzle":
                            self.puzzle_size = 5
                            self.end = True
                        if button.text == "36 Piece Puzzle":
                            self.puzzle_size = 6
                            self.end = True

    def timeTaken(self):
        return self.endTime - self.startTime
    
class washWindow:
    def __init__(self):
        self.end = False
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

    def new(self):
        self.b1 = Button(440, 100, 300, 100, "Start Next", WHITE, BLACK)
        self.screen.fill(BGCOLOUR)
        self.b1.draw(self.screen)
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if self.b1.click(mouse_x, mouse_y):
                    self.end = True
    
    def run(self):
        while not self.end:
            self.events()
        self.endTime = time.time()
        return
    
class participantWindow:
    def __init__(self):
        self.end = False
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.b1 = Button(440, 100, 300, 100, "Start Puzzle", WHITE, BLACK)
        self.input_box = InputBox(440, 250, 300, 50)

    def new(self):
        self.screen.fill(BGCOLOUR)
        self.b1.draw(self.screen)
        self.input_box.draw(self.screen)
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if self.b1.click(mouse_x, mouse_y):
                    self.end = True
                    
            self.input_box.handle_event(event)
    
    def run(self):
        while not self.end:
            self.events()
            self.screen.fill(BGCOLOUR)
            self.b1.draw(self.screen)
            self.input_box.draw(self.screen)
            pygame.display.flip()
        self.endTime = time.time()
        return self.input_box.text

class boredWindow:
    def __init__(self):
        self.end = False
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.font = pygame.font.Font(None, 100)

    def new(self):
        self.buttons_list = []
        self.buttons_list.append(Button(200+20, 300, 150, 100, "1", WHITE, BLACK))
        self.buttons_list.append(Button(200+190, 300, 150, 100, "2", WHITE, BLACK))
        self.buttons_list.append(Button(200+360, 300, 150, 100, "3", WHITE, BLACK))
        self.buttons_list.append(Button(200+530, 300, 150, 100, "4", WHITE, BLACK))
        self.buttons_list.append(Button(200+700, 300, 150, 100, "5", WHITE, BLACK))
        self.screen.fill(BGCOLOUR)
        for i in self.buttons_list:
            i.draw(self.screen)
        
        text = "How bored are you on a scale of"
        x, y = 100, 100
        text = self.font.render(text, True, WHITE)
        text1 = "1 to 5"
        x1, y1 = 550, 170
        text1 = self.font.render(text1, True, WHITE)
        self.screen.blit(text, (x, y))
        self.screen.blit(text1, (x1, y1))
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for button in self.buttons_list:
                    if button.click(mouse_x, mouse_y):
                        if button.text == "1":
                            self.value = 1
                            self.end = True
                        if button.text == "2":
                            self.value = 2
                            self.end = True
                        if button.text == "3":
                            self.value = 3
                            self.end = True
                        if button.text == "4":
                            self.value = 4
                            self.end = True
                        if button.text == "5":
                            self.value = 5
                            self.end = True
    
    def run(self):
        while not self.end:
            self.events()
        return self.value

# a = participantWindow()
# while True:
#     a.new()
#     c = a.run()
#     print(c)           
#     pygame.quit()
#     break
# choice = choiceWindow()
# while True:
#     choice.new()
#     c = choice.run()
#     pygame.quit()
#     print("choice: ",c)
#     print("Time Taken:",choice.timeTaken())
    
#     break            