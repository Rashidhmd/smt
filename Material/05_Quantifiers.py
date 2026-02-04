
# SMT solvers also support problems with quantifiers 

# Example: existence of the opposite of an integer
from z3 import *
x = Int('x')
y = Int('y')
s = Solver()
s.add(ForAll(x, Exists(y, x + y == 0)))
print(s.check())
print(s.model()) # why is this empty?


# Example: existence of neutral element
s2 = Solver()
s2.add(Exists(x, ForAll(y, x + y == y)))
print(s2.check())