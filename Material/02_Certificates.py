from z3 import *
from utils import *
set_param(proof=True)

# check if set_param is set to true
print(f"Proof generation is set to: {get_param('proof')}")

x = Int('x')
y = Int('y')

c1 = (x == 10) 
c2 = (y > x) 

solver = Solver()
solver.add(c1)
solver.add(c2)

has_solution = solver.check()

# Print the solution
if has_solution == sat:
    print(f"\nThe constraints are satisfiable.", end=' ')
    print(f"Solution: \n\t{solver.model()}")
else:
    print(f"\nThe constraints are unsatisfiable")
    print(f"\nProof of unsatisfiability: \n\t", end='')
    print(solver.proof())


c3 = (y < 3)
solver.add(c3)  

has_solution = solver.check()

# Print the solution
if has_solution == sat:
    print(f"\nThe constraints are satisfiable.", end=' ')
    print(f"Solution: \n\t{solver.model()}")
else:
    print(f"\nThe constraints are unsatisfiable")
    print(f"\nProof of unsatisfiability: \n\t", end='')
    print(solver.proof())
