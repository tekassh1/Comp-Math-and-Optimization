# 67% testcases passed

import math

def first_function(args: []) -> float:
    return math.sin(args[0])

def second_function(args: []) -> float:
    return (args[0] * args[1]) / 2

def third_function(args: []) -> float:
    return pow(args[0], 2) * pow(args[1], 2) - 3 * pow(args[0], 3) - 6 * pow(args[1], 3) + 8

def fourth_function(args: []) -> float:
    return pow(args[0], 4) - 9 * args[1] + 2

def fifth_function(args: []) -> float:
    return args[0] + pow(args[0], 2) - 2 * args[1] * args[2] - 0.1

def six_function(args: []) -> float:
    return args[1] + pow(args[1], 2) + 3 * args[0] * args[2] + 0.2

def seven_function(args: []) -> float:
    return args[2] + pow(args[2], 2) + 2 * args[0] * args[1] - 0.3

def default_function(args: []) -> float:
    return 0.0

def get_functions(n: int):
    if n == 1:
        return [first_function, second_function]
    elif n == 2:
        return [third_function, fourth_function]
    elif n == 3:
        return [fifth_function, six_function, seven_function]
    else:
        return [default_function]

def get_vec_max(vec):
    return max(abs(elem) for elem in vec)

def solve_by_fixed_point_iterations(system_id, number_of_unknowns, initial_approximations):
    iters_lim = 1000
    precision = 10**(-5)
    step = precision

    approximation = initial_approximations
    cntr = 0

    system = get_functions(system_id)

    while True:
        new_approximation = []
        try:
            new_approximation = [eq(approximation) for eq in system]
        except OverflowError as err:
            return initial_approximations
        
        diff_vec = [new_approximation[i] - approximation[i] for i in range(len(approximation))]
        cntr += 1
        if (get_vec_max(diff_vec) < precision or cntr >= iters_lim):
            break
        approximation = new_approximation
    
    return approximation