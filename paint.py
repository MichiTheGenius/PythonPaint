import pygame

WIDTH = HEIGHT =  800

WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
ROWS = COLUMNS = 50
PIXEL_SIZE = WIDTH // COLUMNS
run = True

class Pixel():
    def __init__(self,x,y,color,size):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.rect = pygame.Rect(self.x,self.y,self.size,self.size)

    def draw(self,window):
        pygame.draw.rect(window,self.color,self.rect)

    def set_color(self,color):
        self.color = color

def makePixelMatrix():
    matrix = []
    for i in range(ROWS):
        matrix.append([])
        for j in range(COLUMNS):
            matrix[i].append(Pixel(j*PIXEL_SIZE,i*PIXEL_SIZE,WHITE,PIXEL_SIZE))
    return matrix

matrix = makePixelMatrix()
def drawMatrix():
    for i in range(ROWS):
        for j in range(COLUMNS):
            matrix[i][j].draw(WINDOW)

def exitLogic():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = false

current_color = BLACK
def choose_color():
    global current_color
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        current_color = RED
    elif keys[pygame.K_s]:
        current_color = BLACK
    elif keys[pygame.K_b]:
        current_color = BLUE
    elif keys[pygame.K_g]:
        current_color = GREEN


def main_loop():
    while run:
        WINDOW.fill(WHITE)
        drawMatrix()
        exitLogic()
        choose_color()
        print(current_color)
        if pygame.mouse.get_pressed()[0]:
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
            position_on_grid_x = mouseX // PIXEL_SIZE
            position_on_grid_y = mouseY // PIXEL_SIZE
            matrix[position_on_grid_y][position_on_grid_x].set_color(current_color)
        pygame.display.update()
    pygame.quit()

main_loop()
