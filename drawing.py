
import pygame
import math
import numpy

def drawing(obj, canvas, cwidth, cheight, dt):

    L1 = obj.L1
    L2 = obj.L2
    t1 = obj.t1
    t2 = obj.t2
    m1 = obj.m1
    m2 = obj.m2

    P1 = 0.85 * min(cwidth / 2, cheight / 2) * (L1 / (L1 + L2))
    P2 = 0.85 * min(cwidth / 2, cheight / 2) * (L2 / (L1 + L2))

    # Position for each bob (in pixels, pixels)
    X0 = numpy.array([int(cwidth / 2), int(cheight / 2)])
    X1 = X0 + numpy.array([int(P1 * math.sin(t1)), int(P1 * math.cos(t1))])
    X2 = X1 + numpy.array([int(P2 * math.sin(t2)), int(P2 * math.cos(t2))])

    # Colors for rods and bobs
    color_m1 = (255, 0, 0)
    color_m2 = (0, 0, 255)
    color_L1 = (0,0,0)
    color_L2 = (128, 128, 128)

    # For fresh window
    canvas.fill((255, 255, 255))

    # Radius for each bob (in pixels, min 3, max 12)
    R1 = max(3, int(12 * (m1 / (m1 + m2))))
    R2 = max(3, int(12 * (m2 / (m1 + m2))))

    # Drawing rods and bobs to visualize the system
    pygame.draw.line(canvas, color_L1, X0, X1, 3)
    pygame.draw.line(canvas, color_L2, X1, X2, 3)
    pygame.draw.circle(canvas, color_m1, X1, int(R1))
    pygame.draw.circle(canvas, color_m2, X2, int(R2))

    # Showing timestep in the window
    myfont = pygame.font.SysFont("Arial", 15)
    label = myfont.render("dt = %.3g" % dt, 1, (128, 128, 128))
    canvas.blit(label, (10, 10))

    # Updating the screen for every iteration
    pygame.display.flip()
    pygame.display.update()
