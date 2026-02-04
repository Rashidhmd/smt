from z3 import *

def print_solver(solver):
    print(f"\nThe constraints in the solver are: \n\t{solver}")

def check_and_print(solver):
    has_solution = solver.check()
    if has_solution == sat:
        print(f"\nThe constraints are satisfiable.", end=' ')
        print(f"Solution: \n\t{solver.model()}")
        return sat
    else:
        print(f"\nThe constraints are unsatisfiable")
        return unsat

def check_and_print_with_certificate(solver):
    has_solution = solver.check()
    if has_solution == sat:
        print(f"\nThe constraints are satisfiable.", end=' ')
        print(f"Solution: \n\t{solver.model()}")
        return sat
    else:
        print(f"\nThe constraints are unsatisfiable")
        if get_param('proof'):
            print(f"Proof of unsatisfiability:\n{solver.proof()}")
        else:
            print("Proof generation is not enabled.")
        return unsat



def printModelBMC(m):
    m_sorted = sorted ([(d, m[d]) for d in m], key = lambda x: str(x[0]))
    print(*m_sorted,sep='\n')
