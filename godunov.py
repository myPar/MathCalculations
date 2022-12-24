import numpy as np
import plotly as plt
import plotly.graph_objects as go


# scheme Godunov data filling
def fill_graphic(t_steps: int, x_steps: int, h:float, r: int, left_bound:float):
    graphic_data = np.zeros((x_steps, t_steps))

    # initial conditions filling
    for i in range(t_steps):
        graphic_data[0][i] = 3                     # fill u_0^i
    for i in range(x_steps):
        graphic_data[i][0] = 3 if i * h + left_bound <= 0 else 1    # fill u_i^0

    for t in range(1, t_steps):
        for x in range(1, x_steps):
            graphic_data[x][t] = (1 - r) * graphic_data[x][t - 1] + r * graphic_data[x - 1][t - 1]
    
    return graphic_data


def plot_graphics(graphic_data, interval: tuple):
    fig = go.Figure()
    t_steps = graphic_data.shape[1]
    x_steps = graphic_data.shape[0]

    x_data = np.linspace(interval[0], interval[1], x_steps)
    plot_data = np.transpose(graphic_data)

    for t in range(0, t_steps):
        fig.add_trace(go.Scatter(x=x_data, y=plot_data[t], mode='lines+markers', showlegend=False))
    solution = [3 if x_data[i] <= 0 else 1 for i in range(len(x_data))]
    fig.add_trace(go.Scatter(x=x_data, y=solution, mode='lines', showlegend=False))

    fig.show()


def main():
    period = 1
    interval = (-10, 10)
    a = 1
    print("enter h:")
    h = float(input())
    print("enter r:")
    r = float(input())

    tau = r * h / a
    print("tau=" + str(tau))

    t_steps = period / tau + 1
    x_steps = interval[1] * 2 / h
    print(x_steps)
    print(t_steps)
    
    x_steps = int(x_steps)
    t_steps = int(t_steps)
    
    print("x steps = " + str(x_steps))
    print("t steps = " + str(t_steps))
    
    graphic_data = fill_graphic(t_steps, x_steps, h, r, interval[0])
    plot_graphics(graphic_data, interval)


if __name__ == '__main__':
    main()
