import math

def f(x):
    return math.e ** (3 * x) * math.sin(2 * x)
def f_to_string(x):
    return f"e^(3 * {x}) * sin(2 * {x})"

def trapezoidal_method(a, b, n):
    h = round((b - a) / n, 4)
    s = 0.5 * (f(a) + f(b))
    print(f"n = {n}, h = {h}, a = {a}, b = {b}")
    print(f"({f_to_string(a)} + {f_to_string(b)}) / 2 ", end="")
    for i in range(1, n):
        s += f(a + i * h)
        print(f"+ {f_to_string(round(a + i * h, 4))} ", end="")
    print(f"= {round(s, 4)}")

    result = round(h * s, 4)
    print(f"result = {h} * {round(s, 4)} = {result}")

trapezoidal_method(0, round(math.pi / 4, 4), 5)