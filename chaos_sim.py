import pygame
import math
import numpy as np

def draw_pendulums(pendulums, canvas, cwidth, cheight, dt):
    canvas.fill((0, 0, 0))  # Clear the canvas
    
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Colors for each pendulum
    
    for i, obj in enumerate(pendulums):
        L1, L2, t1, t2 = obj.L1, obj.L2, obj.t1, obj.t2
        P1 = 0.85 * min(cwidth / 2, cheight / 2) * (L1 / (L1 + L2))
        P2 = 0.85 * min(cwidth / 2, cheight / 2) * (L2 / (L1 + L2))
        
        X0 = np.array([int(cwidth / 2), int(cheight / 2)])
        X1 = X0 + np.array([int(P1 * math.sin(t1)), int(P1 * math.cos(t1))])
        X2 = X1 + np.array([int(P2 * math.sin(t2)), int(P2 * math.cos(t2))])

        # Draw rods and bobs
        pygame.draw.line(canvas, colors[i], X0, X1, 2)
        pygame.draw.line(canvas, colors[i], X1, X2, 2)
        pygame.draw.circle(canvas, colors[i], X1, 5)
        pygame.draw.circle(canvas, colors[i], X2, 5)
    
    # Update the display
    pygame.display.flip()
    pygame.display.update()
