import pygame as pg
import random as rd

def c_change():
    global c_ant
    if c_ant == 0:
        c_ant = 1
    else:
        c_ant = 0

def turn():
    global c_ant
    global o_ant
    if c_ant == 0:
        o_ant += 1
        if o_ant > 5:
            o_ant -= 4
    else:
        o_ant -=1
        if o_ant < 2:
            o_ant += 4
    bg[ant_x][ant_y] = o_ant

def move():
    global c_ant, bg, ant_y, ant_x, o_ant
    bg[ant_x][ant_y] = c_ant
    if o_ant == 2:
        ant_y -= 1
    elif o_ant == 3:
        ant_x -= 1
    elif o_ant == 4:
        ant_y += 1
    else:
        ant_x += 1

    if ant_x >= BLOCK_NB:
        ant_x -= BLOCK_NB
    elif ant_x < 0:
        ant_x += BLOCK_NB
    elif ant_y >= BLOCK_NB:
        ant_y -= BLOCK_NB
    elif ant_y < 0:
        ant_y += BLOCK_NB

    c_ant = bg[ant_x][ant_y]
    bg[ant_x][ant_y] = o_ant

LENGTH = 800
BLOCK_NB = 20
BLACK_BLOCK = 0
FPS = 20
block_size = int(LENGTH/BLOCK_NB)
end = False
c_ant = 0
o_ant = 2
func = 0

sprites = [0 for i in range(6)]
pg.init()
screen = pg.display.set_mode((LENGTH,LENGTH))
clock = pg.time.Clock()

W = pg.image.load("White.png")
B = pg.image.load("Black.png")
A_u = pg.image.load("Ant_up.png")
A_d = pg.image.load("Ant_down.png")
A_l = pg.image.load("Ant_left.png")
A_r = pg.image.load("Ant_right.png")

W = pg.transform.scale(W,(block_size,block_size))
B = pg.transform.scale(B,(block_size,block_size))
A_u = pg.transform.scale(A_u,(block_size,block_size))
A_d = pg.transform.scale(A_d,(block_size,block_size))
A_l = pg.transform.scale(A_l,(block_size,block_size))
A_r = pg.transform.scale(A_r,(block_size,block_size))

sprites[0] = W
sprites[1] = B
sprites[2] = A_u
sprites[3] = A_l
sprites[4] = A_d
sprites[5] = A_r

bg = [[0 for i in range (BLOCK_NB)] for i in range(BLOCK_NB)]

for i in range (BLACK_BLOCK):
    x = rd.randint(0, BLOCK_NB-1)
    y = rd.randint(0, BLOCK_NB-1)
    bg[y][x] = 1

ant_x = rd.randint(0, BLOCK_NB-1)
ant_y = rd.randint(0, BLOCK_NB-1)

for i in range(BLOCK_NB):
    for j in range(BLOCK_NB):
        val = bg[i][j]
        img = sprites[val]
        screen.blit(img, (i*block_size,j*block_size ))

while not end:
    pg.display.flip()

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                end = True

    if func == 0:
        func = 1
        turn()
        c_change()
    else:
        func = 0
        move()

    for i in range(BLOCK_NB):
        for j in range(BLOCK_NB):
            val = bg[i][j]
            img = sprites[val]
            screen.blit(img, (i*block_size,j*block_size ))

    clock.tick(FPS)

pg.quit()