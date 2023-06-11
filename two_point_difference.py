def forward_difference(f_x, f_forward, h):
    return (f_forward - f_x) / h
def backward_difference(f_x, f_backward, h):
    return (f_x - f_backward) / h

x0 = 1.0
x1 = 1.2
x2 = 1.4

h = 0.2

fx0 = 1.0000
fx1 = 1.2625
fx2 = 1.6595

print(f"f'({x0}) = ({fx1} - {fx0}) / {h} = {round(forward_difference(fx0, fx1, h), 4)}")
print(f"f'({x1}) = ({fx2} - {fx1}) / {h} = {round(forward_difference(fx1, fx2, h), 4)}")
print(f"f'({x2}) = ({fx2} - {fx1}) / {h} = {round(backward_difference(fx2, fx1, h), 4)}")
