import math

def f(x):
    return math.e ** (3 * x) * math.sin(2 * x)
def f_to_string(x):
    return f"e^(3 * {x}) * sin(2 * {x})"

def trapezoidal_method(a, b, n):
    h = round((b - a) / n, 4)
    s = f(a) + f(b)
    print(f"n = {n}, h = {h}, a = {a}, b = {b}")
    print(f"{f_to_string(a)} + {f_to_string(b)} ", end="")
    for i in range(1, n):
        coefficient = 2 if i % 2 == 0 else 4
        s += coefficient * f(a + i * h)
        print(f"+ {coefficient} * {f_to_string(round(a + i * h, 4))} ", end="")
    print(f"= {round(s, 4)}")

    result = round(h / 3 * s, 4)
    print(f"result = {h} / 3 * {round(s, 4)} = {result}")

trapezoidal_method(0, round(math.pi / 4, 4), 4)