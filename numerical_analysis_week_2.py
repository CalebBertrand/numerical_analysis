def f(x):
    return x**3 - 7 *  x**2 + 14 * x - 6

a = 3.2
b = 4
tolerance = 0.01
print(f"Starting interval is {a} to {b}, and our tolerance is {tolerance}")

midpt = (a + b) / 2
while abs(f(midpt)) > tolerance:
     if f(a) * f(midpt) < 0:
          print(f"Since f({a}) * f({midpt}) is negative, we search down this interval")
          b = midpt
          midpt = round((a + midpt) / 2, 5)
     else:
          print(f"Since f({midpt}) * f({b}) is negative, we search down this interval")
          a = midpt
          midpt = round((midpt + b) / 2, 5)
     
     print(f"The new interval becomes {a} to {b}")

print(f"The midpoint is {midpt}, and f({midpt}) is less than our tolerance of {tolerance}, so {midpt} is the answer")