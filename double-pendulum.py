import drawing
import pygame
import math
import pickle
from analysis import analysis

def main():
    t, x_data_1, x_data_2, y_data_1, y_data_2, t1_data, t2_data, K_data, P_data, E_data = [], [], [], [], [], [], [], [], [], []
  
    g= 9.8
    dt= 0.025
    m1= 5
    m2= 1
    t1 =60
    t2=60
    w1=0.5
    w2=1
    L1=1
    L2=1

    cwidth = cheight = 500
    test_mode = False
    from dp_lagrangian import DoublePendulumLagrangian
    obj = DoublePendulumLagrangian(g, m1, m2, t1, t2, w1, w2, L1, L2)
    step = 0

    if not test_mode:
        pygame.init()
        clock = pygame.time.Clock()
        canvas = pygame.display.set_mode((cwidth, cheight))
        pygame.display.set_caption("Double Pendulum")

    index = 0
    while True:
        should_quit = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                should_quit = True

        if should_quit:
            save_data = {
                't': t, 't1_data': t1_data, 't2_data': t2_data,
                'x_data_1': x_data_1, 'y_data_1': y_data_1,
                'x_data_2': x_data_2, 'y_data_2': y_data_2,
                'K_data': K_data, 'P_data': P_data, 'E_data': E_data
            }
            with open('filename.pickle', 'wb') as handle:
                pickle.dump(save_data, handle)
            analysis(t, t1_data, t2_data, x_data_1, x_data_2, y_data_1, y_data_2, K_data, P_data, E_data)
            pygame.quit()
            break

        if not test_mode:
            x1 = L1 * math.sin(obj.t1)
            y1 = -L1 * math.cos(obj.t1)
            x2 = x1 + L2 * math.sin(obj.t2)
            y2 = y1 - L2 * math.cos(obj.t2)

            t.append(index * dt)
            index += 1
            x_data_1.append(x1)
            x_data_2.append(x2)
            y_data_1.append(y1)
            y_data_2.append(y2)
            t1_data.append(obj.t1)
            t2_data.append(obj.t2)
            K_data.append(obj.kinetic_energy())
            P_data.append(obj.potential_energy())
            E_data.append(obj.mechanical_energy())

            drawing.drawing(obj, canvas, cwidth, cheight, dt)

        clock.tick(40)
        obj.time_step(dt)
        step += 1

if __name__ == "__main__":
    main()
