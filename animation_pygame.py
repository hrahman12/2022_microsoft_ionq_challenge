# iQuHACK-quantum-cat
#iQuHACK quantum computing video game


from numpy import tile
import pygame
from pygame.locals import *
from sympy import false

#initialize pygame
pygame.init()

#setting up screen dimensions
screen = pygame.display.set_mode((1220,800))

# background image
bg = pygame.image.load('videogame_Img/start.png')
bg  = pygame.transform.scale(bg, (1220, 800))

#Title and Icon (work on later, have to download a pic first)
pygame.display.set_caption("Pygame practice")
#icon = pygame.image.load('python')
#pygame.display.set_icon(icon)

# making a tile surface to put the p gates on, black and white for now to see tiles
tilesize = 120

def create_board_surf():
    board_surf = pygame.Surface((tilesize*5, tilesize*5))
    dark = False
    for y in range(5):
        for x in range(5):
            rect = pygame.Rect(x*tilesize, y*tilesize, tilesize, tilesize)
            pygame.draw.rect(board_surf, pygame.Color('black'), rect)
    return board_surf

def create_board():
    board = []
    for y in range (5):
        board.append([])
        for x in range (5):
            board[y].append(None)
    return board

# draws a red rectangle on selected square
boardPosition = (320, 140)
def get_square_under_mouse(board):
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos()) - boardPosition
    x, y = [int(v // tilesize) for v in mouse_pos]
    try: 
        if x >= 0 and y >= 0: return (board[y][x], x, y)
    except IndexError: pass
    return None, None, None


# loading and resizing the p gates/pi blocks

pi = pygame.image.load('videogame_Img/pi.png')
pi_2 = pygame.image.load('videogame_Img/pi_2.png')
pi_4 = pygame.image.load('videogame_Img/pi_4.png')
pi_8 = pygame.image.load('videogame_Img/pi_8.png')
pi_16 = pygame.image.load('videogame_Img/pi_16.png') 

pi = pygame.transform.scale(pi, (115, 100))
pi_2 = pygame.transform.scale(pi_2, (115, 100))
pi_4 = pygame.transform.scale(pi_4, (115, 100))
pi_8 = pygame.transform.scale(pi_8, (115, 100))
pi_16 = pygame.transform.scale(pi_16, (115, 100))


# class piBox, created manipulate the position of the image and treat it as a rectangle - no longer necessary
#class piBox(pygame.sprite.Sprite):
#    def __init__(self, pGate, x, y):
#        super().__init__()
#
#        self.image = pGate
#        self.x = x
#        self.y = y
#        self.width = 115
#        self.height = 100
#        self.rect = self.image.get_rect()
#        self.selected = False

#pGate1 = piBox(pi, 10, 10)
#pGate2 = piBox(pi_2, 110, 10)
#pGate3 = piBox(pi_4, 210, 10)
#pGate4 = piBox(pi_8, 310, 10)
#pGate5 = piBox(pi_16, 410, 10)

pGates = [pi, pi_2, pi_4, pi_8, pi_16]

current_pGate = -1
pGate_rects = [pGates[i].get_rect(topleft = (20+40*i, 20)) for i in range(len(pGates))]


#Game loop for quitting screen
board = create_board()
board_surf = create_board_surf()
clock = pygame.time.Clock()
running = True
LeftButton = 0
while running:

    screen.fill(pygame.Color('grey'))

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_rect = pygame.Rect(event.pos, (1, 1))
                current_pGate = mouse_rect.collidelist(pGate_rects)

                #if event.button == 1:            
                    #if pGate1.image.get_rect().collidepoint(event.pos):
                        #rectangle_draging = True
                        #mouse_x, mouse_y = event.pos
                        #offset_x = pGate1.x - mouse_x
                        #offset_y = pGate1.y - mouse_y

            #elif event.type == pygame.MOUSEBUTTONUP:
            #    if event.button == 1:            
            #        rectangle_draging = False

            if event.type == pygame.MOUSEMOTION:
                if event.buttons[LeftButton]:
                    rel = event.rel
                    if 0 <= current_pGate < len(pGates):
                        pGate_rects[current_pGate].x += rel[0]
                        pGate_rects[current_pGate].y += rel[1]

                #if rectangle_draging:
                #    mouse_x, mouse_y = event.pos
                #    pGate1.x = mouse_x + offset_x
                #    pGate1.y = mouse_y + offset_y

    piece, x, y = get_square_under_mouse(board)
    print(x,y)

    
    screen.blit(board_surf, (320, 140))
    screen.blit(bg, (0, 0))
    for i in range(len(pGates)):
        screen.blit(pGates[i], pGate_rects[i])
    if x != None:

        rect = (boardPosition[0] + x * tilesize, boardPosition[1] + y * tilesize, tilesize, tilesize)
        pygame.draw.rect(screen, (255, 0, 0, 50), rect, 2)

    pygame.display.update()
    clock.tick(60)
