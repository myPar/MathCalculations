import sys
import math

# constants and global variables:
exception_exit_code = 1
correct_exit_code = 0

print_calculus = True
calc_types = ['Newton', 'one_tangent', 'secants']


# helping functions:
def get_input_value(exception_message:str, value_type):
    input_value = input()
    
    assert value_type == int or value_type == float

    try:
        input_value = value_type(input_value)
    except ValueError:
        print("invalid value " + input_value + exception_message, file=sys.stderr)
        sys.exit(exception_exit_code)
    
    return input_value


def print_with_flag(flag:bool, header:str, args):
    if flag:
        print(header, end='')

        for i in range(len(args)):
            print(str(args[i]) + " ", end='')
        print()


# help calculation functions:
def get_der_value(x:float):
    return 2*x


def get_function_value(x:float):
    return x**2 - 5


# main calculation functions:
def calc_root_newton(start_point:float, iteration_count:int):
    cur_point = start_point
    
    print_with_flag(print_calculus, "iteration 0: ", [cur_point])

    for i in range(iteration_count):
        cur_point_der_value = get_der_value(cur_point)
        assert cur_point_der_value != 0

        cur_point = cur_point - get_function_value(cur_point) / cur_point_der_value
        print_with_flag(print_calculus, "iteration " + str(i + 1) + ":", [cur_point])
    
    return cur_point


def calc_root_one_tangent(start_point:float, iteration_count:int):
    cur_point = start_point
    start_point_der_value = get_der_value(start_point)
    
    assert start_point_der_value != 0

    print_with_flag(print_calculus, "iteration 0: ", [cur_point])

    for i in range(iteration_count):
        cur_point = cur_point - get_function_value(cur_point) / start_point_der_value
        print_with_flag(print_calculus, "iteration " + str(i + 1) + ":", [cur_point])

    return cur_point


def calc_root_secants(start_point1:float, start_point2:float, iteration_count:int):
    first_point = start_point1
    second_point = start_point2

    function_value1 = get_function_value(first_point)
    function_value2 = get_function_value(second_point)

    assert function_value1 - function_value2 != 0

    print_with_flag(print_calculus, "iteration 0: ", [first_point, second_point])

    for i in range(iteration_count):
        second_point_copy = second_point
        
        second_point = second_point - function_value2 *  \
        (second_point - first_point) / (function_value2 - function_value1)

        first_point = second_point_copy

        print_with_flag(print_calculus, "iteration " + str(i + 1) + ":", [first_point, second_point])
    
    return second_point


# main:
def main()->int:
    args = sys.argv
    assert len(args) == 2

    arg = args[1]

    if arg == 'True':
        print_calculus = True
    elif arg == 'False':
        print_calculus = False
    else:
        print("invalid 'print calculus' flag.\n",file=sys.stderr)
        
        return exception_exit_code
    
    # get number of iterations
    print('enter the number of iterations:')
    iteration_count = get_input_value("should be an int value.", int)

    # get type of the calculation
    print('enter the type of calculation: ')
    
    print_with_flag(True, "", calc_types)
    calc_type = input()

    if calc_type not in calc_types:
        print("invalid calculus type - '" + calc_type, file=sys.stderr)
        
        return exception_exit_code
    else:
        # get start point
        print('enter the start point:')
        start_point = get_input_value("should be a float value.", float)

        if calc_type == calc_types[0]:
            result = calc_root_newton(start_point, iteration_count)
        elif calc_type == calc_types[1]:

            result = calc_root_one_tangent(start_point, iteration_count)
        else:
            # get second start point
            print('enter the second start point:')
            second_start_point = get_input_value("should be a float value.", float)

            result = calc_root_secants(start_point, second_start_point, iteration_count)
            

    print("result point: " + str(result))
    
    print("error=", abs(result - math.sqrt(5)))

    return correct_exit_code


if __name__ == '__main__':
    main()

