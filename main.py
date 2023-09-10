"""
Author: woaby
last modified: 6-9-2023
"""

import pygame as pg
import utils.generate as worldgen
import random

playerX, playerY = (200, 200) # camera starting position
camX, camY = (0, 0)
image_paths = [
    "assets/grass.png", "assets/sand.png",
    "assets/water.png", "assets/darkgrass.png"
]

# initialize pygame window
pg.init()
pg.display.set_caption("Isometric world generation")
surface = pg.display.set_mode((800, 600), 0, 32)

time = pg.time.Clock()
dt = time.tick(60) / 1000

rectWidth, rectHeight = (32, 16)
world = worldgen.init(size=(420, 20), seed=random.randint(0, 500)) # size = (height, width)
worldArr = world.getArr()

# load all the images into a list
images = [pg.image.load(path).convert_alpha() for path in image_paths]

while True:
    surface.fill((0, 0, 0))
    keys = pg.key.get_pressed()

    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            pg.quit()
            exit()
    
    top_chunk = int(camY / rectHeight) - 4
    bottom_chunk = int((camY + surface.get_height()) / rectHeight) - 12

    # Whe only render what is on screen to optimize performance
    for row in range(20):
        for column in range(top_chunk, bottom_chunk):
            tile_xx = row * rectWidth
            tile_yx = column * rectWidth

            tile_xy = row * rectHeight
            tile_yy = column * rectHeight
            
            screen_x = tile_xx - tile_yx - camX
            screen_y = tile_xy + tile_yy - camY

            # Here whe asign our tiles to a number in our generated array
            if 0 <= row < len(worldArr) and 0 <= column < len(worldArr[row]):
                if worldArr[row][column] == 0:
                    surface.blit(images[2], (screen_x, screen_y))
                elif worldArr[row][column] == 1:
                    surface.blit(images[0], (screen_x, screen_y))
                elif worldArr[row][column] == 2:
                    surface.blit(images[1], (screen_x, screen_y))
                elif worldArr[row][column] == 3:
                    surface.blit(images[3], (screen_x, screen_y))
    
    # camera
    camX += ((playerX - surface.get_width()/2) - camX) / 0.5 * dt
    camY += ((playerY - surface.get_height()/2) - camY) / 0.5 * dt

    # movement camera (player)
    if keys[pg.K_w]:
        playerY -= 200 * dt
        playerX += 400 * dt
    elif keys[pg.K_s]:
        playerY += 200 * dt
        playerX -= 400 * dt
        
    pg.display.update()
    time.tick(60)
