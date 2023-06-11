import math

def f(x):
    return -x**3 - math.cos(x)
def f_prime_estimate(x0, x1):
    return (f(x1) - f(x0)) / (x1 - x0)
def f_to_string(x):
    return f"-{x}**3 - cos({x})"

i = 1
guess = -1
next_guess = 0

print(f"p0 is {guess} and p1 is {next_guess}")

while (i < 3):
    i = i + 1

    f_prime = round(f_prime_estimate(guess, next_guess), 5)
    estimate_function = f"({f_to_string(next_guess)} - ({f_to_string(guess)})) / ({next_guess} - {guess})"
    print(f"estimate of f'({guess}) is {estimate_function} = {f_prime}")

    guess = next_guess
    next_guess = round(guess - f(guess) / f_prime, 5)
    print(f"p{i} is {guess} - ( ({f_to_string(guess)}) / ({f_prime}) ) = {next_guess}")

print(f"p{i} = {next_guess}")
