import math
import decimal

f = lambda x : pow(x, 4) + pow(x, 2) + x + 1

a, b, eps = -1, 0, 0.003

def get_derivative(x, eps):
    return (f(x + eps) - f(x - eps))/(2 * eps)

def get_second_derivative(x, eps):
    return (f(x + eps) - 2*f(x) + f(x - eps))/(pow(eps, 2))

def half_division_method(a, b, eps):
    while (b - a >= 2*eps):
        x1 = (a + b - eps)/2
        x2 = (a + b + eps)/2
        leftEps = f(x1)
        rightEps = f(x2)

        if (leftEps > rightEps): 
            a = x1
        else: 
            b = x2

    return (a + b)/2

def golden_ratio_method(a, b, eps):
    fi = (1 + math.sqrt(5))/2
    x1 = b - (b - a)/fi
    x2 = a + (b - a)/fi

    while ((b - a)/2 >= eps):
        if (f(x1) > f(x2)):
            a = x1
            x1 = x2
            x2 = b - (x1 - a)
        else:
            b = x2
            x2 = x1
            x1 = a + (b - x2)

    return (a + b)/2

def chords_method(a, b, eps):
    a_der = get_derivative(a, eps)
    b_der = get_derivative(b, eps)

    while True:
        x = a - (a_der/(a_der - b_der)) * (a - b)
        x_der = get_derivative(x, eps)

        if (x_der <= eps):
            return x    
        
        if (x_der > 0):
            b = x
            b_der = x_der
        else:
            a = x
            a_der = x_der

def newton_method(a, b, eps):
    x0 = b
    x0_der = get_derivative(x0, eps)
    x0_s_der = get_second_derivative(x0, eps)
    x = x0 - (x0_der / x0_s_der)

    while (True):
        x_der = get_derivative(x, eps)

        if (abs(x_der) < eps):
            break
        x = x - x_der / get_second_derivative(x, eps)
    
    return x

print(half_division_method(a, b, eps))
print(golden_ratio_method(a, b, eps))
print(chords_method(a, b, eps))
print(newton_method(a, b, eps))