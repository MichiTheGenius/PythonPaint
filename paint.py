import pygame

WIDTH = 800
HEIGHT = 600
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
PIXEL_SIZE = int(input("Enter desired pixel size: "))

ROWS = HEIGHT // PIXEL_SIZE + 5
COLUMNS = WIDTH // PIXEL_SIZE + 5 # a bit of tolerance
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

def main_loop():
    while run:
        WINDOW.fill(WHITE)
        drawMatrix()
        exitLogic()
        if pygame.mouse.get_pressed()[0]:
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
            position_on_grid_x = mouseX // PIXEL_SIZE
            position_on_grid_y = mouseY // PIXEL_SIZE
            matrix[position_on_grid_y][position_on_grid_x].set_color(BLACK)
        pygame.display.update()
    pygame.quit()

main_loop()
