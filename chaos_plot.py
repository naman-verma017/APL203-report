import matplotlib.pyplot as plt
import pickle

def plot_chaos(t, t2_data):
    colors = ['r', 'g', 'b']
    plt.figure()
    for i, data in enumerate(t2_data):
        plt.plot(t, data, colors[i], label=f'Pendulum {i + 1}')
    plt.xlabel("Time")
    plt.ylabel("Theta 2")
    plt.title("Theta 2 vs Time (Chaos)")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    with open('chaos_data.pickle', 'rb') as handle:
        data = pickle.load(handle)
        plot_chaos(data['t'], data['t2_data'])
