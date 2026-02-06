
## Exam

# Consider the following Counting game:
#
# A player draws 6 different numbers. The goal is to combine these numbers using the elementary arithmetic operations (+, -, *, /) to obtain a number as close as possible to a given goal. 
# Combining numbers means the following. First, the player chooses an initial number from the starting six numbers in their hand. Then, they choose a second number from their hand (different from the initial one), together with an operation, and compute the result of the operation. Now they choose a third number from their hand (different from the first and the second number), an operation, and compute the results. And so on.
#
# For example, if the user draws the numbers 1, 3, 5, 8, 10 e 50, and the goal number is 462, they can combine their numbers in the following way:
#
# 8 + 1 = 9
# 9 * 50 = 450
# 450 + 10 = 460
# 460 - 3 = 457
# 457 + 5 = 462
#
# Here, the player precisely reached the goal number. However, there are cases in which this is not possible. In such cases, the player has to aim to find the closest possible number to the goal.
# If it is possible to precisely reach the goal number, the players should try to minimize the numbers used. E.g., in the previous game, a better solution would have been:
#
# 50 - 3 = 47
# 47 * 10 = 470
# 470 - 8 = 462 
#
# which only uses 4 numbers instead of 6.
#
# Each number can only be used one time. 
#
# Your task is to implement a function CountingStrategy() that takes as input a list of 6 user numbers and 1 goal number, and returns the winning strategy. 
# The winning strategy should be printed in the following form:
#   Initial number: <n1>
#   Step 1: operation <operation> with number <n2> -> result <r2>
#   Step 2: operation <operation> with number <n3> -> result <r3>
#   ...
#   Final number: <final_result>
#   Distance from goal: <distance>
#
#
# E.g.:
# CountingStrategy([1, 3, 5, 8, 10, 50], 462) should output:
#   Initial number: 50
#   Step 1: operation - with number 3 -> result 47
#   Step 2: operation * with number 10 -> result 470
#   Step 3: operation - with number 8 -> result 462
#   Final number: 462
#   Distance from goal: 0
#

from z3 import *

# Create a list of integer variables x_0, x_1, ..., x_9
x = [Int(f'x_{i}') for i in range(6)] 
goal = Int('goal')

# Create a datatype to represent the functions f and g
Function = Datatype('Functions')
Function.declare('add')
Function.declare('sub')
Function.declare('mul')
Function.declare('div')
Function = Function.create()

# Create a list of variables to represent the function applied at each step
function = [Const("f_%s" % (i), Function) for i in range(6)]

def add(x_now1, x_now2, x_next):
    return x_next == x_now1 + x_now2

def sub(x_now1, x_now2, x_next):
    return x_next == x_now1 - x_now2

def mul(x_now1, x_now2, x_next):
    return x_next == x_now1 * x_now2

def div(x_now1, x_now2, x_next):
    return x_next == x_now1 / x_now2

def CountingStrategy(x, goal):
    # Create the solver
    s = Solver()

    # Add the initial state constraint
    initial_state = x[0] == 0
    s.add(initial_state)
    for i in range(5):
        transition = Or(
            And(function[i] == Function.add, add(x[i], x[i+1])),
            And(function[i] == Function.sub, sub(x[i], x[i+1])),
            And(function[i] == Function.mul, mul(x[i], x[i+1])),
            And(function[i] == Function.div, div(x[i], x[i+1])),
        )
        s.add(transition) 
        s.add(x[i+1] != x[i])  
        # check if property P is satisfied at step i+1
        status = s.check(x[i+1] == goal)  # add the property constraint
        if status == sat:
            print(f"Property satisfied at step {i+1}")
            #print(s.model())
            #printModelBMC(s.model())
            break


# [Optional]
# After you have implemented the function to find the optimal strategy for the Counting game, consider the following variation of the game.
# The rules are as before, but now an adversary can "attack" the player after their last operation. 
# The attack consists in choosing one number between 1 and 10, and replace it to the user choosen last number to make the final result as far as possible from the goal number.
# E.g., in the previous example, the attacker would have replaced the last number 8 with the number 0, making the player final result be 470 - 0 = 470.
# Hence, in this variant, the player must find a strategy that is resilient to the actions of the attacker. The best strategy will not be the one that gets closest to the goal, but rather the one that, after the worst possible attack, is as close as possible to the goal. 
#
#
# Your task is to implement a function CountingStrategyResilient that takes the same input as CountingStrategy, and returns the optimal strategy for this variation.
# In the output, include:
#    Distance from goal after attack: <distance_after_attack>