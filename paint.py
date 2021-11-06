import pygame

WIDTH = 800
HEIGHT = 600
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
RED = (255,0,0)
PIXEL_SIZE = 10
run = True
ROWS = 10
COLUMS = 10

matrix = []
for i in range(ROWS):
    matrix.append([])
    for j in range(COLUMS):
        matrix[i].append(1)
print(matrix)
class Pixel():
    def __init__(self,x,y,color,size):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.rect = pygame.Rect(self.x,self.y,self.size,self.size)
    def draw(self,window):
        pygame.draw.rect(window,self.color,self.rect)
p = Pixel(0,0,RED,PIXEL_SIZE)
while run:
    WINDOW.fill(WHITE)
    p.draw(WINDOW)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = false
    pygame.display.update()

pygame.quit()
