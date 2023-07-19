# credits:
# some of this code and assets was taken from DaFluffyPotato (grass block image | public domain)

import random
import sys
import pygame
from pygame.locals import *

def main():
    pygame.init()
    size = pygame.display.Info()
    pygame.display.gl_set_attribute(pygame.GL_ACCELERATED_VISUAL, 1)
    window = pygame.display.set_mode((size.current_w, size.current_h))
    pygame.display.set_caption("The Legendary Lotl")

    screen = pygame.display.set_mode((size.current_w, size.current_h),0,32)
    display = pygame.Surface((int(size.current_w/2.5), int(size.current_h/1.4)))
    clock = pygame.time.Clock()

    # map image
    grass_img = pygame.image.load("assets/grass.png").convert_alpha()
    grass_img.set_colorkey((0, 0, 0))

    #initialize assets
    init_kelp_list = [pygame.image.load("assets/kelp 1.png").convert_alpha(), pygame.image.load("assets/kelp 2.png").convert_alpha(), pygame.image.load("assets/kelp 3.png").convert_alpha(), pygame.image.load("assets/kelp 4.png").convert_alpha(), pygame.image.load("assets/kelp 5.png").convert_alpha(), pygame.image.load("assets/kelp 6.png").convert_alpha(), pygame.image.load("assets/kelp 7.png").convert_alpha(), pygame.image.load("assets/kelp 8.png").convert_alpha(), pygame.image.load("assets/kelp 9.png").convert_alpha(), pygame.image.load("assets/kelp 10.png").convert_alpha(), pygame.image.load("assets/kelp 11.png").convert_alpha(), pygame.image.load("assets/kelp 12.png").convert_alpha(), pygame.image.load("assets/kelp 13.png").convert_alpha(), pygame.image.load("assets/kelp 14.png").convert_alpha(), pygame.image.load("assets/kelp 15.png").convert_alpha(), pygame.image.load("assets/kelp 16.png").convert_alpha()]
    init_lotl_list = [pygame.image.load("assets/Lotl 1.png").convert_alpha(), pygame.image.load("assets/Lotl 2.png").convert_alpha(), pygame.image.load("assets/Lotl 3.png").convert_alpha(), pygame.image.load("assets/Lotl 4.png").convert_alpha(), pygame.image.load("assets/Lotl 5.png").convert_alpha(), pygame.image.load("assets/Lotl 6.png").convert_alpha(), pygame.image.load("assets/Lotl 7.png").convert_alpha(), pygame.image.load("assets/Lotl 8.png").convert_alpha(), pygame.image.load("assets/Lotl 9.png").convert_alpha(), pygame.image.load("assets/Lotl 10.png").convert_alpha(), pygame.image.load("assets/Lotl 11.png").convert_alpha(), pygame.image.load("assets/Lotl 12.png").convert_alpha(), pygame.image.load("assets/Lotl 13.png").convert_alpha(), pygame.image.load("assets/Lotl 14.png").convert_alpha(), pygame.image.load("assets/Lotl 15.png").convert_alpha(), pygame.image.load("assets/Lotl 16.png").convert_alpha()]

    kelp_list = []
    lotl_list = []

    for lotl in init_kelp_list:
        kelp_list.append(pygame.transform.scale(lotl, (size.current_w / 25, size.current_h / 10)))

    for lotl in init_lotl_list:
        lotl_list.append(pygame.transform.scale(lotl, (size.current_w / 20, size.current_h / 25)))

    init_tile_map = [["air",0,-30],["air",30,-15],["air",60,0],["air",90,15],["air",120,30],["air",150,45],["air",180,60],["air",210,75],
                     ["air",-30,-15],["air",0,0],["air",30,15],["air",60,30],["air",90,45],["air",120,60],["air",150,75],["air",180,90],
                     ["air",-60,0],["air",-30,15],["air",0,30],["air",30,45],["air",60,60],["air",90,75],["air",120,90],["air",150,105],
                     ["air",-90,15],["air",-60,30],["air",-30,45],["air",0,60],["air",30,75],["air",60,90],["air",90,105],["air",120,120],
                     ["air",-120,30],["air",-90,45],["air",-60,60],["air",-30,75],["air",0,90],["air",30,105],["air",60,120],["air",90,135],
                     ["air",-150,45],["air",-120,60],["air",-90,75],["air",-60,90],["air",-30,105],["air",0,120],["air",30,135],["air",60,150],
                     ["air",-180,60],["air",-150,75],["air",-120,90],["air",-90,105],["air",-60,120],["air",-30,135],["air",0,150],["air",30,165],
                     ["air",-210,75],["air",-180,90],["air",-150,105],["air",-120,120],["air",-90,135],["air",-60,150],["air",-30,165],["air",0,180],
                     ]

    tile_map = init_tile_map[:]

    lotl_x = size.current_w / 15
    lotl_y = size.current_h / 30

    frame_tracker = 0
    lotl_frame = 0

    while True:
        frame_tracker += 1
        if frame_tracker == 5:
            if lotl_frame + 1 < len(lotl_list):
                lotl_frame += 1

            else:
                lotl_frame = 0

            frame_tracker = 0

        display.fill((0,128,128))  
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                move = False

                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == K_DOWN:
                    lotl_y += 30

                if event.key == K_LEFT:
                    lotl_x -= 30
                            
                if event.key == K_RIGHT:
                    lotl_x += 30
                            
                if event.key == K_UP:
                    lotl_y -= 30

        for x in range(1,int(size.current_w/30),3):
            for y in range(1,int(size.current_h/30),3):
                display.blit(grass_img, (size.current_w / 6 + x * 10 - y * 10, size.current_h / 6 + x * 5 + y * 5))

        display.blit(lotl_list[lotl_frame], (lotl_x, lotl_y))

        screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))

        pygame.display.flip()
        clock.tick(60)

main()
