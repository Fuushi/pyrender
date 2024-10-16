class calc():
    def getAngle(point1, point2): #(x, y, z) <- y is vertical, x is north, z is east
        #0, 0 is directly along x
        import math
        alpha = -((math.atan2((point1[0] - point2[0]), (point1[2] - point2[2])) * 180) / 3.1415926535) - 90
        #alpha is along the reference plane

        beta =  -((math.atan2((point1[0] - point2[0]), (point1[1] - point2[1])) * 180) / 3.1415926535) - 90

        return(alpha, beta)

    def angleToSC(alpha, beta, width, height, FOV):
        #use highest of width and height as scalar
        import math

        #print(FOV)

        greaterResolution = (int(width > height) * width) + (int(height >= width) * height)

        #print(greaterResolution)

        projection_plane_distance = math.sin(90 - (FOV / 2)) / (math.sin((FOV / 2)) / (greaterResolution / 2))

        #now i just need to project the vertex onto the plane
        #print(projection_plane_distance)
        #x = int(
        #    math.sin(alpha) / (
        #    math.sin(90 - alpha) / 
        #    projection_plane_distance
        #))
        temp = 28.9
        x = int(math.sin(alpha / temp) * (width / 2))
        #print('x:', x, ', alpha:', alpha)
        #y = int(
        #    math.sin(beta) / (
        #    math.sin(90 - beta) / 
        #    projection_plane_distance
        #))
        y = int(math.sin(beta / temp) * (height / 2))
        #print('y:', y, ', beta: ', beta)
        #print(projection_plane_distance)
        return((x + (width / 2)), (y + (height / 2)))

        
        #^should return the greater resolution without branchingV