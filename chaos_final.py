import pygame
import math
import pickle
from dp_lagrangian import DoublePendulumLagrangian
from chaos_sim import draw_pendulums
from chaos_plot import plot_chaos

def main():
    g = 9.8
    dt = 0.025
    m1, m2 = 2, 2
    t1 = math.radians(90)  
    t2_initials = [math.radians(101.1), math.radians(101.11), math.radians(101.12)]  
    w1, w2 = 0.5, 1
    L1, L2 = 2, 1
    cwidth = cheight = 500

    pendulums = [DoublePendulumLagrangian(g, m1, m2, t1, t2, w1, w2, L1, L2) for t2 in t2_initials]
    
    t = []
    t2_data = [[] for _ in range(len(pendulums))]
    
    pygame.init()
    clock = pygame.time.Clock()
    canvas = pygame.display.set_mode((cwidth, cheight))
    pygame.display.set_caption("Double Pendulum Chaos")

    running = True
    index = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        t.append(index * dt)
        for i, obj in enumerate(pendulums):
            obj.time_step(dt)
            t2_data[i].append(math.degrees(obj.t2))
    
        draw_pendulums(pendulums, canvas, cwidth, cheight, dt)
        clock.tick(40)
        index += 1
    
    chaos_data = {'t': t, 't2_data': t2_data}
    with open('chaos_data.pickle', 'wb') as handle:
        pickle.dump(chaos_data, handle)
    
    pygame.quit()
    plot_chaos(t, t2_data)

if __name__ == "__main__":
    main()
