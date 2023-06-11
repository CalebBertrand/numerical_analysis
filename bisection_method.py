def f(x):
    return 3 * (x + 1) * (x - 0.5) * (x - 1)

a = -1.25
b = 2.5
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