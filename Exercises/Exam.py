
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

# 8 + 1 = 9
# 9 * 50 = 450
# 450 + 10 = 460
# 460 - 3 = 457
# 457 + 5 = 462

# 
# x[0] + 1 = x[1]
# x[1] * 50 = x[2]
# x[2] + 10 = x[3]
# x[3] - 3 = x[4]
# x[4] + 5 = x[5]

# lista di numeri [1,2,3] e lista di stati ottenuti [3,6]
# x[0] = 1
# x[1] = 2
# x[0] uno di quei numeri

# numero iniziale x[0] uno tra quelli
# x[1] prende un valore tra quelli(3) e fa l'operazione - e ottiene 47 
# prende il risultato precedente e un valore tra quelli(10) e fa l'operazione * e ottiene 470
# prende il risultato precedente e un valore tra quelli(8) e fa l'operazione - e ottiene 462
# 

# x1 + x2 = add(x1, x2)
# 9 * 50 = 450
# 450 + 10 = 460
# 460 - 3 = 457
# 457 + 5 = 462


from z3 import *
MAX_NUMBERS = 6

# Create a list of integer variables x_0, x_1, ..., x_9
user_numbers = [Int(f'num_{i}') for i in range(MAX_NUMBERS)]
x = [Int(f'x_{i}') for i in range(MAX_NUMBERS)] 
goal = 462

# Create a datatype to represent the functions f and g
Function = Datatype('Functions')
Function.declare('add')
Function.declare('sub')
Function.declare('mul')
Function.declare('div')
Function = Function.create()

# Create a list of variables to represent the function applied at each step
function = [Const("f_%s" % (i), Function) for i in range(MAX_NUMBERS - 1)]

def add(x1, x2, x_next):
    return x_next == x1 + x2

def sub(x1, x2, x_next):
    return x_next == x1 - x2

def mul(x1, x2, x_next):
    return x_next == x1 * x2

def div(x1, x2, x_next):
    return x_next == x1 / x2


# CountingStrategy([1, 3, 5, 8, 10, 50], 462) should output:
#   Initial number: 50
#   Step 1: operation - with number 3 -> result 47
#   Step 2: operation * with number 10 -> result 470
#   Step 3: operation - with number 8 -> result 462
#   Final number: 462
#   Distance from goal: 0
def printModelBMC(m):
    op = {"div": "/", "mul":"*", "sub":"-", "add": "+"}

    print("Initial number: ", m[user_numbers[0]])
    for i in range(MAX_NUMBERS-1):
        if m[function[i]] == None: break
        
        print(f"Step {i+1}: operation {op[str(m[function[i]])]} with number {m[user_numbers[i+1]]} -> result: {m[x[i+1]]}")

def CountingStrategy(numbers=[1, 3, 5, 6, 4, 2], goal=56):
    # Create the solver
    s = Solver()

    # Add the initial state constraint
    initial_state = Or(user_numbers[0]==numbers[0], user_numbers[0]==numbers[1], user_numbers[0]==numbers[2], user_numbers[0]==numbers[3], user_numbers[0]==numbers[4], user_numbers[0]==numbers[5])
    initial_state1 = x[0] == user_numbers[0]

    # constraint that each number chosen is different
    distinct_numbers =  Distinct(user_numbers) 


    s.add(initial_state)
    s.add(initial_state1)
    s.add(distinct_numbers)

    for i in range(MAX_NUMBERS-1):
        selected_number = Or(user_numbers[i+1]==numbers[0], user_numbers[i+1]==numbers[1], user_numbers[i+1]==numbers[2], user_numbers[i+1]==numbers[3], user_numbers[i+1]==numbers[4], user_numbers[i+1]==numbers[5]) 
        transition = Or(
            And(function[i] == Function.add, add(x[i], user_numbers[i+1], x[i+1])),
            And(function[i] == Function.sub, sub(x[i], user_numbers[i+1], x[i+1])),
            And(function[i] == Function.mul, mul(x[i], user_numbers[i+1], x[i+1])),
            And(function[i] == Function.div, div(x[i], user_numbers[i+1], x[i+1])),
        )
        s.add(transition) 
        s.add(selected_number)
        
        # check if property P is satisfied at step i+1
        status = s.check(x[i+1] == goal)  # add the property constraint
        if status == sat:
            print(f"Property satisfied at step {i+1}")
            printModelBMC(s.model())
            break

CountingStrategy()




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