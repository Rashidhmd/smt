from utils import printModelBMC

# Model Checking problem:
# Given
#  - a set of states S
#  - a transition relation T : S -> S
#  - a set of initial states I 
#  - a property P 
# Is there a path from an initial state to a state that satisfies P?


# Bounded Model Checking problem:
# same as the Model Checking problem but with a bound k on the length of the path


# Example:
# Given the functions
#   f(x) = x + 17
#   g(x) = 13 * x
# and the property P : 345 < x < 349
# Is there a sequence (of length at most 10) of applications of f and g starting from 0
# that leads to a value of x that satisfies P?

from z3 import *

# Create a list of integer variables x_0, x_1, ..., x_9
x = [Int(f'x_{i}') for i in range(10)] 

# Create a datatype to represent the functions f and g
Function = Datatype('Functions')
Function.declare('f')
Function.declare('g')
Function = Function.create()

# Create a list of variables to represent the function applied at each step
function = [Const("f_%s" % (i), Function) for i in range(10)]

# Python function that express the relation between x_now and x_next under f (just for readability)
def f(x_now, x_next):
    return x_next == x_now + 17

# Same for g
def g(x_now, x_next):
    return x_next == 13 * x_now

# Define the initial state
initial_state = x[0] == 0

# Create the solver
s = Solver()

# Add the initial state constraint
s.add(initial_state)

# Add the transition relation constraints
for i in range(9):
    transition = Or(
        And(function[i] == Function.f, f(x[i], x[i+1])),
        And(function[i] == Function.g, g(x[i], x[i+1]))
    )
    s.add(transition)   
    # check if property P is satisfied at step i+1
    s.push()  # save the current state of the solver
    status = s.check(And(x[i+1] > 335, x[i+1] < 345))  # add the property constraint
    if status == sat:
        print(f"Property satisfied at step {i+1}")
        #print(s.model())
        printModelBMC(s.model())
        break

