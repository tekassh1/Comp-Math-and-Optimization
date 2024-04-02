from math import *

f = lambda x, y: pow(x, 4) + pow(y, 4) - 2 * pow(x - y, 2)

f_x_der = lambda x, y: 4 * pow(x, 3) - 4 * x + 4 * y
f_y_der = lambda x, y: 4 * pow(y, 3) + 4 * x - 4 * y

norm = lambda vec: sqrt(pow(vec[0], 2) + pow(vec[1], 2))

def grad_desc(x, y):
    prec = 0.0001
    step = 1

    while True:
        grad = [f_x_der(x, y), f_y_der(x, y)]
        new_x = x - step * grad[0]
        new_y = y - step * grad[1]

        if (abs(f(new_x, new_y) - f(x, y)) < prec):
            x = new_x
            y = new_y
            break
        
        if (f(new_x, new_y) > f(x, y)):
            step /= 10
            continue

        x = new_x
        y = new_y

    return f(x, y)

def steepest_desc(x, y):
    eps = 0.0001
    grad = [f_x_der(x, y), f_y_der(x, y)]
    normed_grad = norm(grad)

    while (norm(grad) >= eps):
        s_k = [grad[0] / normed_grad, grad[1] / normed_grad]
        
        l = -2.5
        r = 2.5

        while (r - l >= 2 * eps):
            x1 = (l + r - eps) / 2
            x2 = (l + r + eps) / 2

            left_eps = f(x + x1 * s_k[0], y + x1 * s_k[1])
            right_eps = f(x + x2 * s_k[0], y + x2 * s_k[1])

            if (left_eps >= right_eps):
                l = x1
            else:
                r = x2

        x_m = (l + r) / 2
        x = x + x_m * s_k[0]
        y = y + x_m * s_k[1]
        grad = [f_x_der(x, y), f_y_der(x, y)]
        normed_grad = norm(grad)

    return f(x, y)

print(grad_desc(-0.2, 0.2))
print(steepest_desc(-0.2, 0.2))