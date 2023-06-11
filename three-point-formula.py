def three_point_endpoint(fx0, fx1, fx2, h):
    print(f"(-3 * ({fx0}) + 4 * ({fx1}) - {fx2}) / (2 * {h}) = ", end="")
    return (-3 * fx0 + 4 * fx1 - fx2) / (2 * h)

def three_point_midpoint(fx0, fx2, h):
    print(f"({fx2} - {fx0}) / (2 * {h}) = ", end="")
    return (fx2 - fx0) / (2 * h)

x0 = -2.7
x1 = -2.5
x2 = -2.3
x3 = -2.1

fx0 = 0.054797
fx1 = 0.11342
fx2 = 0.65536
fx3 = 0.98472

h = 0.2
precision = 5

print(f"f'({x0}), using three-point endpoint method: ")
print(round(three_point_endpoint(fx0, fx1, fx2, h), precision))

print(f"f'({x1}), using three-point midpoint method: ")
print(round(three_point_midpoint(fx0, fx2, h), precision))

print(f"f'({x2}), using three-point midpoint method: ")
print(round(three_point_midpoint(fx1, fx3, h), precision))

print(f"f'({x3}) using three-point endpoint method with a negative h:")
print(round(three_point_endpoint(fx3, fx2, fx1, -h), precision))