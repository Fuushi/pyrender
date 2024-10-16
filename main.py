import sys
from dep import *

import pygame
from pygame.locals import * #?
    #probly gonna switch this out for another graphics library
    #if im feeling retarted i might just create my own winAPI handler

##rander main

#ENVIORONMENT VARIABLES
FOV = 70 #70 degrees
CAMERA_POSITION = (-10, 0, 0)
CAMERA_ROTATION = (0, 0, 0) #towards origin



##rendering engine
pygame.init() #run this code in an init class
fps = 120
fpsClock = pygame.time.Clock() 
width, height = 1000,1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Randy Engine')



def __main__():
    try:    
        #load object
        # ^assign object data to an object class
        game_objects = [fileIO.load_obj("cube1.obj")] #important note, objects can be returned
            #serialize into tuple or array
        #game_objects.append(fileIO.load_obj("sphere1.obj"))
        game_objects.append(fileIO.load_obj("sphere1.obj"))
        game_objects[1].pos = [0, 0, 0]

        print(game_objects)
        #print(game_objects[0].V_A)
        

        while True:
            ##logic
            screen.fill((0, 0, 0))

            game_objects[0].pos[0] -= 0.02

            if game_objects[0].pos[0] <= -30:
                game_objects[0].pos[0] = 0
            


            #render call
            render.edge_render(screen, pygame, game_objects, FOV, width, height)
            render.vertex_render(screen, pygame, game_objects, FOV, width, height) #pass in geometry when thats ready
            
            #event handler
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()
            fpsClock.tick(fps)


        wait = input()
        return()
    except Exception as error:
        print(error)
        wait = input()



if __name__ == '__main__':
    print('entering main')
    __main__()
    print('exiting runtime')