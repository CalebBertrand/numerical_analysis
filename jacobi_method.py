# a)
# x1 = (1 + x2 - x3) / 3
# x2 = (-2 * x3 -3 * x1) / 6
# x3 = (4 - 3 * x2 - 3 * x1) / 7

equations_a = {
    'x1': {
        'function': lambda x: (1 + x[1] - x[2]) / 3,
        'to_string': lambda x: f"(1 + {x[1]} - {x[2]}) / 3"
    },
    'x2': {
        'function': lambda x: (-2 * x[2] - 3 * x[0]) / 6,
        'to_string': lambda x: f"(-2 * {x[2]} - 3 * {x[0]}) / 6"
    },
    'x3': {
        'function': lambda x: (4 - 3 * x[1] - 3 * x[0]) / 7,
        'to_string': lambda x: f"(4 - 3 * {x[1]} - 3 * {x[0]}) / 7"
    }
}

# b)
# x1 = (9 + x2) / 10
# x2 = (7 + 2 * x3 +  x1) / 10
# x3 = (9 + 2 * x2) / 10

equations_b = {
    'x1': {
        'function': lambda x: (9 + x[1]) / 10,
        'to_string': lambda x: f"(9 + {x[1]}) / 10"
    },
    'x2': {
        'function': lambda x: (7 + 2 * x[2] + x[0]) / 10,
        'to_string': lambda x: f"(7 + 2 * {x[2]} + {x[0]}) / 10"
    },
    'x3': {
        'function': lambda x: (9 + 2 * x[1]) / 10,
        'to_string': lambda x: f"(9 + 2 * {x[1]}) / 10"
    }
}

# c)
# x1 = (6 - 5*x2) / 10
# x2 = (25 -5*x1 +4*x3) / 10
# x3 = (-11 + 4*x2 + x4) / 8
# x4 = (-11 + x3) / 5

equations_c = {
    'x1': {
        'function': lambda x: (6 - 5 * x[1]) / 10,
        'to_string': lambda x: f"(6 - 5 * {x[1]}) / 10"
    },
    'x2': {
        'function': lambda x: (25 - 5 * x[0] + 4 * x[2]) / 10,
        'to_string': lambda x: f"(25 - 5 * {x[0]} + 4 * {x[2]}) / 10"
    },
    'x3': {
        'function': lambda x: (-11 + 4 * x[1] + x[3]) / 8,
        'to_string': lambda x: f"(-11 + 4 * {x[1]} + {x[3]}) / 8"
    },
    'x4': {
        'function': lambda x: (-11 + x[2]) / 5,
        'to_string': lambda x: f"(-11 + {x[2]}) / 5"
    }
}

# d)
# x1 = (6 - x2 - x3 - x5) / 4
# x2 = (6 + x1 - x3 - x4) / 3
# x3 = (6 - 2*x1 - x2 + x4 + x5) / 5
# x4 = (6 + x1 + x2 + x3) / 4
# x5 = (6 - 2*x2 + x3 - x4) / 4

equations_d = {
    'x1': {
        'function': lambda x: (6 - x[1] - x[2] - x[4]) / 4,
        'to_string': lambda x: f"(6 - {x[1]} - {x[2]} - {x[4]}) / 4"
    },
    'x2': {
        'function': lambda x: (6 + x[0] - x[2] - x[3]) / 3,
        'to_string': lambda x: f"(6 + {x[0]} - {x[2]} - {x[3]}) / 3"
    },
    'x3': {
        'function': lambda x: (6 - 2 * x[0] - x[1] + x[3] + x[4]) / 5,
        'to_string': lambda x: f"(6 - 2 * {x[0]} - {x[1]} + {x[3]} + {x[4]}) / 5"
    },
    'x4': {
        'function': lambda x: (6 + x[0] + x[1] + x[2]) / 4,
        'to_string': lambda x: f"(6 + {x[0]} + {x[1]} + {x[2]}) / 4"
    },
    'x5': {
        'function': lambda x: (6 - 2 * x[1] + x[2] - x[3]) / 4,
        'to_string': lambda x: f"(6 - 2 * {x[1]} + {x[2]} - {x[3]}) / 4"
    }
}

def jacobi_method(x, equations, n):
    print(f"n = {n}, x = {x}")
    for i in range(n):
        print()
        x_new = []
        for key in equations.keys():
            x_new.append(round(equations[key]['function'](x), 4))
            print(f"{key} = {equations[key]['to_string'](x)} = {x_new[-1]}")
        x = x_new
        print(f"x = {x}")

    print()
    x_stringified = ', '.join(['x' + str(i+1) for i in range(len(x))])
    x_values_strinified = ', '.join(map(lambda n: str(n), x))
    print(f"Final values for {x_stringified}: {x_values_strinified}")
    return x

print("a)")
jacobi_method([0, 0, 0], equations_a, 2)
print()

print("b)")
jacobi_method([0, 0, 0], equations_b, 2)
print()

print("c)")
jacobi_method([0, 0, 0, 0, 0], equations_c, 2)
print()

print("d)")
jacobi_method([0, 0, 0, 0, 0], equations_d, 2)
print()