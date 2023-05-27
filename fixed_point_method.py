import math

def g(x):
    return -math.pow(1 - 2 * x, 1.0 / 3)

# Note: this method only works if f(x) has a negative derivative over the interval that the guess and root are in
guess = 0.5
next_guess = round(g(guess), 5)
tolerance = 0.001
circuit_break_count = 0

print(f"We will assume a tolerance of {tolerance}")
print(f"Initial guess: {guess}")
print(f"g({guess}) = {next_guess}")

while(circuit_break_count < 25 and abs(guess - next_guess) > tolerance):
    print(f"| {guess} - {next_guess} | is more than {tolerance}, so we iterate again.")
    guess = next_guess
    next_guess = round(g(next_guess), 5)
    circuit_break_count = circuit_break_count + 1
    print(f"The next guess will be g({guess}) = {next_guess}")

if circuit_break_count < 25:
    print(f"| {guess} - {next_guess} | is less than {tolerance}, so we are done. The answer is {next_guess}")
else:
    print("We iterated over 25 times and couldn't find the answer. It probably diverges.")