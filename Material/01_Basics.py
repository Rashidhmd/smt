from z3 import *

# Declaring a real variable x with name 'x' (names are only used for printing)
x = Int('x')

# Declaring an integer variable y with name 'y'
y = Int('y')

# Declaring a constraint 'c1' that expresses the condition 'x is smaller than y'
c1 = (x < y) 

# Declaring a constraint 'c2' that expresses the condition 'y is equal to x plus 10'
c2 = (y == x + 10) 

# This is an alternative equivalent definition of c2
# c2 = (x + 10 == y) 

# Also this is an alternative equivalent definition of c2
# c2 = (10 == y - x) 

# '==' is not an assignment, but a relation between terms !



# Declaring a solver
solver = Solver()

# Let's add the constraints c1 and c2 to the solver
solver.add(c1)
solver.add(c2)

def print_solver(solver):
    print(f"\nThe constraints in the solver are: \n\t{solver}")

# print_solver(solver)




# Check if the conjunction of the constraints has a solution
# i.e., if there exist values of x and y that satisfy both c1 and c2
has_solution = solver.check()

# Print the solution
if has_solution == sat:
    print(f"\nThe constraints are satisfiable.", end=' ')
else:
    print(f"\nThe constraints are unsatisfiable")


# Let's add a third constraint c3
c3 = (x**2 == y)

# Recompute the solution
has_solution = solver.check()

# Print the solution
if has_solution == sat:
    print(f"\nThe constraints are satisfiable.", end=' ')
else:
    print(f"\nThe constraints are unsatisfiable")
