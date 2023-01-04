import numpy as np
import plotly.graph_objects as go


def forward(a, b, c, f, n:int):
    alpha_arr = np.zeros((n - 1,))
    betta_arr = np.zeros((n - 1,))

    alpha_arr[0] = 0
    betta_arr[0] = 0

    for i in range(1, n - 1):
        alpha_arr[i] = b / (c - a * alpha_arr[i - 1])
        betta_arr[i] = (f + a * betta_arr[i - 1]) / (c - a * alpha_arr[i - 1])

    return alpha_arr, betta_arr


def backward(a, b, c, n: int, alpha_arr, betta_arr):
    result_vector = np.zeros((n,))

    result_vector[n - 1] = 0

    for i in range(n - 2, 0, -1):
        result_vector[i] = alpha_arr[i] * result_vector[i + 1] + betta_arr[i]
    
    return result_vector


def plot_solutions(solution_vector, n:int):
    assert len(solution_vector) == n
    fig = go.Figure()
    x_solution_arr = np.linspace(0, 1, 10000)
    y_solution_arr = -(x_solution_arr ** 2) + x_solution_arr

    x_approximation_arr = np.linspace(0, 1, n)

    fig.add_trace(go.Scatter(x=x_solution_arr, y=y_solution_arr, mode='lines', name='solution'))
    fig.add_trace(go.Scatter(x=x_approximation_arr, y=solution_vector, mode='lines+markers', name='approximation'))
    fig.show()


def main():
    print("enter n:")
    n = int(input())
    print("n="+str(n))

    print("equation - u'(x) = -2")
    print("solution - u(x) = -x^2 + x")
    solution_vector = np.ones((n,)) * -2
    h = 1 / (n - 1)

    a = -1 / h**2
    b = -1 / h**2
    c = -2 / h**2
    f = -2

    alpha_arr, betta_arr = forward(a, b, c, f, n)

    approximation = backward(a, b, c, n, alpha_arr, betta_arr)    
    plot_solutions(approximation, n)

if __name__ == '__main__':
    main()
    
