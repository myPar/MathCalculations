import math


def calc_integral_sympson(a:float, b:float, f, delta:float) -> float:
    assert a < b
    intervals_count = int((b - a) // (2 * delta))

    result = 0

    for i in range(intervals_count):
        x_1 = a + i * 2 * delta
        x_2 = x_1 + delta
        x_3 = x_2 + delta

        s_i = (delta / 3) * (f(x_3) + 4 * f(x_2) + f(x_1))
        
        result += s_i
    
    x_1_last = a + intervals_count * 2 * delta

    # add last term if any
    if x_1_last < b:
        new_delta = (b - x_1_last) / 2
        result += (delta / 3) * (f(b) + 4 * f(x_1_last + new_delta) + f(x_1_last))

    return result


def calc_integral_trapezoid(a:float, b:float, f, delta:float):
    assert a < b
    intervals_count = int((b - a) // delta)

    result = 0

    for i in range(intervals_count):
        x_1 = a + i * delta
        x_2 = x_1 + delta

        s_i = delta * (f(x_1) + f(x_2)) / 2

        result += s_i
    
    x_1_last = a + intervals_count * delta

    if x_1_last < b:
        result += delta * (f(x_1_last) + f(b)) / 2
    
    return result


def calc_method_info(h:float, calculation_funciton):
    sin_integral = 1
    a = 0
    b = math.pi / 2

    result = calculation_funciton(a, b, math.sin, h)
    result_accurate = calculation_funciton(a, b, math.sin, h/2)
    degree = (result - sin_integral) / (result_accurate - sin_integral)
    
    print("h = " + str(h) + " integral value = " + str(result))
    print("approximation degree = " + str(degree))
    print()


def print_info(mode: str, h_1:float, h_2:float):
    if mode == "sympson":
        calculation_function = calc_integral_sympson
    elif mode == "trapezoid":
        calculation_function = calc_integral_trapezoid

    sin_integral = 1

    print(mode + ":")
    calc_method_info(h_1, calculation_function)
    calc_method_info(h_2, calculation_function)


def main():
    a = 0.0
    b = math.pi / 2
    h_1 = math.pi / (200)
    h_2 = math.pi / (2000)

    modes = ["sympson", "trapezoid"]
    print_info(modes[0], h_1, h_2)
    print_info(modes[1], h_1, h_2)


if __name__ == '__main__':
    main()

