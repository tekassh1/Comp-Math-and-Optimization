# 100% testcases passed

x_values = list(map(float, input().split()))
y_values = list(map(float, input().split()))
x = float(input())

def lagrange_polynomial(x, x_values, y_values):
    if (x_values == 0 or y_values == 0): 
        return 0
    
    if (len(x_values) > len(y_values)):
        x_values = x_values[0 : len(y_values)]
    elif (len(x_values) < len(y_values)):
        y_values = y_values[0 : len(x_values)]

    polynomial_value = 0

    for i in range(len(y_values)):
        curr_basis = 1

        for j in range(len(x_values)):
            if (i != j):
                curr_basis *= (x - x_values[j])/(x_values[i] - x_values[j])

        polynomial_value += y_values[i]*curr_basis
    
    return polynomial_value

print(lagrange_polynomial(x, x_values, y_values))