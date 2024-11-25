import pickle
import matplotlib.pyplot as plt

def analysis(t, t1_data, t2_data, x_data_1, x_data_2, y_data_1, y_data_2, K_data, P_data, E_data):
    
    plt.figure()
    plt.title('x data')
    plt.plot(t, x_data_1, 'r', label='First Pendulum')
    plt.plot(t, x_data_2, 'b', label='Second Pendulum')
    plt.xlabel("Time")
    plt.ylabel("x position")
    plt.legend()
    plt.show()

    plt.figure()
    plt.title('y data')
    plt.plot(t, y_data_1, 'r', label='First Pendulum')
    plt.plot(t, y_data_2, 'b', label='Second Pendulum')
    plt.xlabel("Time")
    plt.ylabel("y position")
    plt.legend()
    plt.show()

    plt.figure()
    plt.title('t1 vs t2')
    plt.plot(t1_data, t2_data)
    plt.xlabel("Theta 1")
    plt.ylabel("Theta 2")
    plt.show()

    plt.figure()
    plt.title("Time vs Theta 1")
    plt.plot(t, t1_data, 'r')
    plt.xlabel("Time")
    plt.ylabel("Theta 1")
    plt.show()

    plt.figure()
    plt.title("Time vs Theta 2")
    plt.plot(t, t2_data, 'b')
    plt.xlabel("Time")
    plt.ylabel("Theta 2")
    plt.show()

    plt.figure()
    plt.plot(t, K_data, 'r', label='Kinetic Energy')
    plt.plot(t, P_data, 'g', label='Potential Energy')
    plt.plot(t, E_data, 'k', label='Mechanical Energy')
    plt.xlabel('Time')
    plt.ylabel('Energy')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    with open('filename.pickle', 'rb') as handle:
        data = pickle.load(handle)
        analysis(
            data['t'], data['t1_data'], data['t2_data'],
            data['x_data_1'], data['x_data_2'],
            data['y_data_1'], data['y_data_2'],
            data['K_data'], data['P_data'], data['E_data']
        )
