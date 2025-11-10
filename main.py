import pygame
import math
import time
import numpy as np
import matplotlib.cm as cm

pygame.init()
pixel_speed = 100
sources = [(500,500, 50), (300,300,50)]

t = time.time()

def calculatevalue(px, py, t):
    #i_time = time.time() - t
    i_time = t
    intensity = 0
    for i in sources:
        x, y, wavelength = i
        intensity += math.sin(2*math.pi*(pixel_speed * i_time - math.dist((x, y), (px, py)))/wavelength)
    return intensity

def recordframe(time, surface):
    pygame.image.save(surface, f"{(time*60)//1}.png")
    print(f"{i}th Image rendered!!!")

def calculatesurf(x, y, t):
    values = np.zeros((x,y))
    for i in range(x):
        for j in range(y):
            values[i][j] = calculatevalue(i,j,t)

    vmax, vmin = values.max(), values.min()

    if vmax == vmin:
        values = np.zeros_like(values)
    else:
        values = (values - vmin)/(vmax - vmin)

    colormap = cm.get_cmap('seismic')(values)
    values = (colormap[:,:,:3]*255).astype(np.uint8)
    return pygame.surfarray.make_surface(values)
    

screen = pygame.display.set_mode((800,800))

def draw(time):
    # s = calculatesurf(800,800, time)
    # screen.blit(s)
    recordframe(time, calculatesurf(800,800, time))
    # pygame.display.flip()

for i in range(100):
    draw((i+1)/60)

while True:
    for e in pygame.event.get():
        if(e.type == pygame.QUIT):
            pygame.quit()
            break
