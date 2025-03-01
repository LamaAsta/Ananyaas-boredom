import pygame
import random
import time
from sprite import *
from settings import *


class Image:  # Capitalize class names for better style
    def __init__(self, path, n):
        self.path = path
        self.image = pygame.image.load(path)
        self.n = n

    def get_dim(self):
        im_obj = self.image.get_rect()
        width_unit = im_obj.width // self.n  # Integer division is important
        height_unit = im_obj.height // self.n
        return height_unit,width_unit
    
    def resize_image(self):
        d = self.get_dim()
        s = 1
        if d[1] > 700:
            s = d[1]/700
        elif d[0]>1000:
            s = d[0]/1000
        # a = (int(d[0]*s),int(d[1]*s))
        self.image = pygame.transform.smoothscale_by(self.image,0.5)
        

    def split_image(self):
        (height_unit, width_unit) = self.get_dim()
        pieces = []
        for i in range(self.n):
            pieces.append([])
            for j in range(self.n):
                crop_x = width_unit * j
                crop_y = height_unit * i
                rect = pygame.Rect(crop_x, crop_y, width_unit, height_unit)
                cropped_surface = self.image.subsurface(rect)
                pieces[i].append(cropped_surface)
        return pieces
    

class Game:
    def __init__(self,path = IPATH,n=3):
        pygame.init()
        self.n = n
        self.base_image = Image(path,n)
        self.base_image.resize_image()
        self.pieces = self.base_image.split_image()
        self.dim = self.base_image.get_dim()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.shuffle_time = 0
        self.start_shuffle = False
        self.previous_choice = ""
        self.start_game = False
        self.start_timer = False
        self.elapsed_time = 0
        self.high_score = float(self.get_high_scores()[0])
        self.time = time.time()
        self.completed = 0

    def get_high_scores(self):
        with open("high_score.txt", "r") as file:
            scores = file.read().splitlines()
        return scores

    def save_score(self):
        with open("high_score.txt", "w") as file:
            file.write(str("%.3f\n" % self.high_score))
 
    def create_game(self):
        grid = [[x + y * self.n for x in range(1, self.n + 1)] for y in range(self.n)]
        grid[-1][-1] = 0
        self.pieces = self.base_image.split_image()
        return grid

    def shuffle(self):
        possible_moves = []
        for row, tiles in enumerate(self.tiles):
            for col, tile in enumerate(tiles):
                if tile.text == "empty":
                    if tile.right():
                        possible_moves.append("right")
                    if tile.left():
                        possible_moves.append("left")
                    if tile.up():
                        possible_moves.append("up")
                    if tile.down():
                        possible_moves.append("down")
                    break
            if len(possible_moves) > 0:
                break
        
        if self.previous_choice == "right":
            possible_moves.remove("left") if "left" in possible_moves else possible_moves
        elif self.previous_choice == "left":
            possible_moves.remove("right") if "right" in possible_moves else possible_moves
        elif self.previous_choice == "up":
            possible_moves.remove("down") if "down" in possible_moves else possible_moves
        elif self.previous_choice == "down":
            possible_moves.remove("up") if "up" in possible_moves else possible_moves

        choice = random.choice(possible_moves)
        self.previous_choice = choice
        # print(choice,col)
        if choice == "right" and col<self.n-1:
            self.tiles_grid[row][col], self.tiles_grid[row][col + 1] = self.tiles_grid[row][col + 1], self.tiles_grid[row][col]
            self.pieces[row][col], self.pieces[row][col + 1] = self.pieces[row][col + 1], self.pieces[row][col]
        elif choice == "left" and col>0:
            self.tiles_grid[row][col], self.tiles_grid[row][col - 1] = self.tiles_grid[row][col - 1], self.tiles_grid[row][col]
            self.pieces[row][col], self.pieces[row][col - 1] = self.pieces[row][col - 1], self.pieces[row][col]
        elif choice == "up" and row>0:
            self.tiles_grid[row][col], self.tiles_grid[row - 1][col] = self.tiles_grid[row - 1][col], self.tiles_grid[row][col]
            self.pieces[row][col], self.pieces[row - 1][col] = self.pieces[row - 1][col], self.pieces[row][col]
        elif choice == "down" and row<self.n-1:
            self.tiles_grid[row][col], self.tiles_grid[row + 1][col] = self.tiles_grid[row + 1][col], self.tiles_grid[row][col]
            self.pieces[row][col], self.pieces[row + 1][col] = self.pieces[row + 1][col], self.pieces[row][col]

    def draw_tiles(self):
        self.tiles = []
        for row, x in enumerate(self.tiles_grid):
            self.tiles.append([])
            for col, tile in enumerate(x):
                if tile != 0:
                    self.tiles[row].append(Tile(self, col, row, str(tile),self.dim,self.n,self.pieces[row][col]))
                else:
                    self.tiles[row].append(Tile(self, col, row, "empty",self.dim,self.n))

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.tiles_grid = self.create_game()
        self.tiles_grid_completed = self.create_game()
        self.elapsed_time = 0
        self.start_timer = False
        self.start_game = False
        self.buttons_list = []
        self.buttons_list.append(Button(700, 100, 200, 50, "Shuffle", WHITE, BLACK))
        self.buttons_list.append(Button(700, 170, 200, 50, "Reset", WHITE, BLACK))
        self.buttons_list.append(Button(700, 240, 200, 50, "End Game", WHITE, BLACK))
        self.draw_tiles()


    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        return self.completed

    def update(self):
        if self.start_game:
            if self.tiles_grid == self.tiles_grid_completed:
                self.start_game = False
                self.playing = False
                self.completed = 1
                if self.high_score > 0:
                    self.high_score = self.elapsed_time if self.elapsed_time < self.high_score else self.high_score
                else:
                    self.high_score = self.elapsed_time
                self.save_score()
            

            if self.start_timer:
                self.timer = time.time()
                self.start_timer = False
            self.elapsed_time = time.time() - self.timer

        if self.start_shuffle:
            self.shuffle()
            self.draw_tiles()
            self.shuffle_time += 1
            if self.shuffle_time > 60:
                self.start_shuffle = False
                self.start_game = True
                self.start_timer = True

        self.all_sprites.update()

    def draw_grid(self):
        for row in range(-1, self.n * self.dim[1], self.dim[1]):
            pygame.draw.line(self.screen, LIGHTGREY, (row, 0), (row, self.n * self.dim[0]))
        for col in range(-1, self.n * self.dim[0], self.dim[0]):
            pygame.draw.line(self.screen, LIGHTGREY, (0, col), (self.n * self.dim[0], col))

    def draw(self):
        self.screen.fill(BGCOLOUR)
        self.all_sprites.draw(self.screen)
        self.draw_grid()
        
        for button in self.buttons_list[:-1]:
            button.draw(self.screen)
        if time.time()-self.time>60*QUIT_MINUTES:
            self.buttons_list[-1].draw(self.screen)
        UIElement(550, 35, "%.3f" % self.elapsed_time).draw(self.screen)
        # UIElement(430, 300, "High Score - %.3f" % (self.high_score if self.high_score > 0 else 0)).draw(self.screen)
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for row, tiles in enumerate(self.tiles):
                    for col, tile in enumerate(tiles):
                        if tile.click(mouse_x, mouse_y):
                            if tile.right() and col<self.n and self.tiles_grid[row][col + 1] == 0:
                                self.tiles_grid[row][col], self.tiles_grid[row][col + 1] = self.tiles_grid[row][col + 1], self.tiles_grid[row][col]
                                self.pieces[row][col], self.pieces[row][col + 1] = self.pieces[row][col + 1], self.pieces[row][col]
                            if tile.left() and col>0 and self.tiles_grid[row][col - 1] == 0:
                                self.tiles_grid[row][col], self.tiles_grid[row][col - 1] = self.tiles_grid[row][col - 1], self.tiles_grid[row][col]
                                self.pieces[row][col], self.pieces[row][col - 1] = self.pieces[row][col - 1], self.pieces[row][col]
                            if tile.up() and row>0 and self.tiles_grid[row - 1][col] == 0:
                                self.tiles_grid[row][col], self.tiles_grid[row - 1][col] = self.tiles_grid[row - 1][col], self.tiles_grid[row][col]
                                self.pieces[row][col], self.pieces[row - 1][col] = self.pieces[row - 1][col], self.pieces[row][col]
                            if tile.down() and row<self.n and self.tiles_grid[row + 1][col] == 0:
                                self.tiles_grid[row][col], self.tiles_grid[row + 1][col] = self.tiles_grid[row + 1][col], self.tiles_grid[row][col]
                                self.pieces[row][col], self.pieces[row + 1][col] = self.pieces[row + 1][col], self.pieces[row][col]
                            self.draw_tiles()

                for button in self.buttons_list:
                    if button.click(mouse_x, mouse_y):
                        if button.text == "Shuffle":
                            self.shuffle_time = 0
                            self.start_shuffle = True
                        if button.text == "Reset":
                            self.new()
                        if button.text == "End Game":
                            self.playing = False

game = Game(n = 3)
# while True:
#     game.new()
#     game.run()
