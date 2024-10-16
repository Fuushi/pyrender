from calc import calc


camera_pos = (-10, 0, 0)
camera_rot = (0, 0, 0) #000 should be forwards along the x

vertex_pos = (0, 10, 10)

FOV = 90#degrees
RESX, RESY = 1000, 1000
#vertex should render directly infront of camera 

alpha, beta = calc.getAngle(camera_pos, vertex_pos)

print(alpha, beta)

x, y = calc.angleToSC(alpha, beta, RESX, RESY, FOV)

print(x, y)

