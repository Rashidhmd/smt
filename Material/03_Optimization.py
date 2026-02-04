from z3 import *
from utils import *

# Find Optimal values

# 02.9 Find the smallest integer greater than 130 that can be written as a sum of squares
#   x = a**2 + b**2

n = Int('x')
a = Int('a')
b = Int('b')
s = Solver()
s.add(a > 0, b > 0)
s.add(n > 130)
s.add(n == a**2 + b**2)

has_solution = check_and_print(s)

while check_and_print(s) == sat:
    m = s.model()
    s.add(n < m[n])  # look for a smaller solution




# Model Counting

# 02.12 Find in how many different ways 128 can be written as a sum of squares

s2 = Solver()
s2.add(n == a**2 + b**2)
s2.add(n == 128)

counter = 0
# print("\nFinding number of solutions:")
# while check_and_print(s2) == sat:
#     counter += 1
#     m = s2.model()
#     s2.add(Or(a != m[a], b != m[b]))  # exclude current solution
# print(f"\nNumber of solutions: {counter}")