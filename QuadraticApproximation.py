import random

f = lambda x : pow(x, 4) + pow(x, 2) + x + 1

a, b = -1, 0
eps = 0.0001

x1 = random.uniform(a, b)
x2 = 0
x3 = 0
fmin = 0
xmin = 0
skip = False

while True:
    if (not skip):
        x2 = x1 + eps
        f1 = f(x1)
        f2 = f(x2)

        if f1 > f2:
            x3 = x1 + 2 * eps
        else:
            x3 = x1 - eps

        f3 = f(x3)

    if (f1 <= f2 and f1 <= f3):
        fmin = f1
        xmin = x1
    elif (f2 <= f1 and f2 <= f3):
        fmin = f2
        xmin = x2
    elif (f3 <= f1 and f3 <= f2):
        fmin = f3
        xmin = f3
    
    numerator = ((x2 ** 2 - x3 ** 2) * f1 + (x3 ** 2 - x1 ** 2) * f2 + (x1 ** 2 - x2 ** 2) * f3)
    denominator = ((x2 - x3) * f1 + (x3 - x1) * f2 + (x1 - x2) * f3)

    if (denominator == 0):
        x1 = xmin
        continue

    maybe_x = 0.5 * (numerator / denominator)
    f_maybe_x = f(maybe_x)

    if (((fmin - f_maybe_x) / f_maybe_x) < eps) and (((xmin - maybe_x) / maybe_x) < eps):
        print(maybe_x)
        break
    elif (maybe_x >= x1 and maybe_x <= x3):
        f2 = f_maybe_x
        x2 = maybe_x

        if (maybe_x <= x2):
            f3 = f2
            x3 = x2
        elif (maybe_x > x2):
            f1 = f2
            x1 = x2
        skip = True
    else:
        x1 = maybe_x
        skip = False