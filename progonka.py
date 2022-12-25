import numpy as np
import plotly.graph_objects as go

def calc_three_diag_matrix(n:int, h:int):
    assert h > 0
    result = np.zeros((n,n))

    result[0][0] = -2 / (h**2)
    result[0][1] = 1 / (h**2)

    for i in range(1, n - 1):
        bias = i - 1
        result[i][bias] = 1 / (h**2)
        result[i][bias + 1] = -2 / (h**2)
        result[i][bias + 2] = 1 / (h**2)
    
    result[n - 1][n - 2] = 1 / (h**2)
    result[n - 1][n - 1] = -2 / (h**2)

    return result

def forward(three_diag_matrix, n:int, solution_vector):
    alpha_arr = np.zeros((n,))
    betta_arr = np.zeros((n,))

    alpha_arr[0] = -three_diag_matrix[0][1] / three_diag_matrix[0][0]
    betta_arr[0] = solution_vector[0] / three_diag_matrix[0][0]

    for i in range(1, n - 1):
        bias = i - 1
        b_i = -three_diag_matrix[i][bias + 2]
        a_i = -three_diag_matrix[i][bias]
        c_i = three_diag_matrix[i][bias + 1]
        alpha_arr[i] = b_i/(c_i - a_i * alpha_arr[i - 1])
        betta_arr[i] = (solution_vector[i] + a_i * betta_arr[i - 1]) / (c_i - a_i * alpha_arr[i - 1])
    c_n = three_diag_matrix[n - 1][n - 1]
    a_n = -three_diag_matrix[n - 1][n - 2]
    f_n = solution_vector[n - 1]

    alpha_arr[n - 1] = c_n / a_n
    betta_arr[n - 1] = -f_n / a_n
    print(alpha_arr)
    print(betta_arr)
    return alpha_arr, betta_arr


def backward(three_diag_matrix, n: int, solution_vector, alpha_arr, betta_arr):
    result_vector = np.zeros((n,))
    a_n = -three_diag_matrix[n - 1][n - 2]
    c_n = three_diag_matrix[n - 1][n - 1]

    #result_vector[n - 1] = (solution_vector[n - 1] + betta_arr[n - 2] * a_n) / (c_n - alpha_arr[n - 2] * a_n)
    result_vector[n - 1] = 0

    for i in range(n - 2, -1, -1):
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
    h = 1 / n
    three_diag_matrix = calc_three_diag_matrix(n, h)
    print(three_diag_matrix)
    print(solution_vector)
    alpha_arr, betta_arr = forward(three_diag_matrix, n, solution_vector)
    approximation = backward(three_diag_matrix, n, solution_vector, alpha_arr, betta_arr)    

    plot_solutions(approximation, n)

if __name__ == '__main__':
    main()
    

