class fileIO():
    def load_obj(filename):
        import os
        from objectGeneric import serialize, game_object, object_math

        here = os.path.dirname(os.path.abspath(__file__)) #the fact that i need this makes me mad but my enviornment is messed so fuck me i guess

        filename = os.path.join(here, filename)

        with open(filename, 'r') as fp: #move this loader into another function
            data = fp.readlines()
        #print(len(data))

        objectInstance = game_object()
        game_object.V_A, game_object.VT_A, game_object.VN_A, game_object.F_A = serialize.de_serialize(data)

        game_object.pos = [0, 0, 0]
        game_object.rot = [0, 0, 0]
        #print("game_object: ", game_object)
        return(game_object)

    def load_mtl(filename):
        return()

#put render class in this file


#for rendering i dont need to render pixel by pixel, rather face by face
#and vertex by vertex, just need to figure out occlusion 
    #for simple occlusion go by average vertex distance from camera
    #figure out a better plan

    
class render(): #probly just a method class
    def vertex_render(screen, pygame, game_objects, FOV, width, height): #<-try passing in pygame instead of reloading
        
        #print(FOV)
        from calc import calc
        import random
        from objectGeneric import object_math

        mx, my = pygame.mouse.get_pos()
        CAM_POS = (-10, 0, 0)
        CAM_ROT = (0, 0, 0) #not yet considered

        VERTEX_POS = (0, 0, 0)
        
        RESX, RESY = width, height

        #print(mx, my)


        #rendering 
        #screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 255, 255), (mx, my), 2)

        #pygame.draw.polygon(screen, (255, 0, 255), [(0, 0), (100, 100), (100, 200)])
    
        #goemetry rendering
        for object in game_objects:#for occlusion, create depth maps and do masking
            #just get vertex rendering for now, face rendering will take more mental
            #print(object.V_A)

            for vertex in object.V_A:


                ##rendering single vertex
                #)
                #print(vertex)
                vertex2 = object_math.apply_pos(vertex, object.pos)
                alpha, beta = calc.getAngle(CAM_POS, vertex2)
                
                #patchwork solution
                #alpha = alpha * (abs(alpha) <= 45)
                #beta = beta * (abs(beta) <= 45)

                #slow solution
                if (abs(alpha) >= 40):
                    continue
                if (abs(beta) >= 40):
                    continue

                x, y = calc.angleToSC(alpha, beta, RESX, RESY, FOV)
                #print(alpha, beta, x, y)

                pygame.draw.circle(screen, (random.randint(100, 255), 30, 30), (x, y), 1)
        return(screen)


    def edge_render(screen, pygame, game_objects, FOV, width, height):
        from calc import calc
        from objectGeneric import object_math
        #print('rendering edge')
        mx, my = pygame.mouse.get_pos()
        CAM_POS = (-10, 0, 0)
        CAM_ROT = (0, 0, 0) #not yet considered
        
        for object in game_objects:#for occlusion, create depth maps and do masking
            #just get vertex rendering for now, face rendering will take more mental
            #print(object.V_A)
            
            for face in object.F_A:
                #print(face)
                #print(len(face))
                vertexArray = []
                for i in range(len(face)):
                    vertexArray.append(
                        object.V_A[face[i][0]]
                    )
                    pass
                
                #print(vertexArray)
                #now i need to convert verted quads to SC quads
                
                
                scArray = []
                for vertex in vertexArray:
                    #print(vertex)
                    vertex2 = object_math.apply_pos(vertex, object.pos)
                    alpha, beta = calc.getAngle(CAM_POS, vertex2)

                    #alpha += 10

                    if (abs(alpha) >= 40):#FUCK SHIT, <- slow solution
                        alpha = 90 #currently causes visual glitches
                                   #while part of an edge is off screen
                    if (abs(beta) >= 40):
                        beta = 90 #Continue, 

                    x, y = calc.angleToSC(alpha, beta, width, height, FOV)

                    scArray.append((x, y))
                
                #print(scArray)

                #each face contains indices for vertex(s)
                #draw lines between them 2 at a time in order
                    #ie 1-2, 2-3, 3-4, 4-1 <- assuming a quad, account for tris


                #render
                if len(scArray) == 4:
                    ##
                    pygame.draw.aaline(screen, (30, 30, 30), scArray[0], scArray[1], 1)
                    pygame.draw.aaline(screen, (30, 30, 30), scArray[1], scArray[2], 1)
                    pygame.draw.aaline(screen, (30, 30, 30), scArray[2], scArray[3], 1)
                    pygame.draw.aaline(screen, (30, 30, 30), scArray[3], scArray[1], 1)
                     #^^swap for aaline
                else:
                    #print("NON-QUAD DETECTED ", len(scArray))
                    pygame.draw.aaline(screen, (30, 30, 30), scArray[0], scArray[1], 1)
                    pygame.draw.aaline(screen, (30, 30, 30), scArray[1], scArray[2], 1)
                    pygame.draw.aaline(screen, (30, 30, 30), scArray[2], scArray[0], 1)
                    
                    #wait = input()
                #print('lines drawn')

                
                pass
        
        
        
        
        
        
        return()