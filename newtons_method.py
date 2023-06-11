import math

def f(x):
    return -x**3 - math.cos(x)
def f_prime(x):
    return -3 * x**2 + math.sin(x)

def f_to_string(x):
    return f"-{x}**3 - cos({x})"
def f_prime_to_string(x):
    return f"-3 * {x}**2 + sin({x})"

def calculate_next_guess(x):
    f_result = round(f(x), 6)
    f_prime_result = round(f_prime(x), 6)
    print(f"f({x}) = {f_to_string(x)} = {f_result}")
    print(f"f'({x}) = {f_prime_to_string(x)} = {f_prime_result}")

    result = round(x - f_result / f_prime_result, 6)
    print(f"p{i} is {x} - {f_result} / {f_prime_result} = {result}")
    print()
    return result

i = 0
guess = 0
print(f"p0 (initial guess) is {guess}")

tolerance = 0.0001
print(f"tolerance is {tolerance}")

next_guess = calculate_next_guess(guess)

while (i < 2):
    i = i + 1
    guess = next_guess
    next_guess = calculate_next_guess(guess)

print(f"p{i} = {next_guess}")