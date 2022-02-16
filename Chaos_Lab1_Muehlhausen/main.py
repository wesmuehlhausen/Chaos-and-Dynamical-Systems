from sympy import *
import numpy as np
from scipy.misc import derivative

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def f(x):
    return x**2 + 1

def function(id, option, x):
    # z = Symbol('z')
    # y = 0

    if id == 'a' and option == 1:
        return (x * x) + 0.25
    elif id == 'a' and option == 2:
        print(f'\n--------------------------------------')
        print(f'Equation: y = x^2 + 0.25 | Seed: {x}')
        print(f"Real fixed point: 0.5")
    elif id == 'a' and option == 3:
        result = derivative(f, 1, dx=1e-6)
        print(result)
        # y = z ** 2 + 0.25
        # yprime = y.diff(1)
        # print(yprime)



def calculate_orbit(seed, loop_count, equation_number):
    # TODO: Adapt it to go until 10^-8 sensitivity is met, not loop_count

    # Init Variables
    x = seed

    # Loop through function given seen value loop_count number of times
    for i in range(loop_count):
        try:
            print(f'{i}) {x}')
            x = function(equation_number, 1, x)
        except:
            print("Error in finding fixed point")
            break

    # Resulting Values
    fixed_point = x


    # Print values
    function(equation_number, 2, -1)
    print(f'Calculated fixed point: {fixed_point}')
    function(equation_number, 3, -1)





# Run here:
if __name__ == '__main__':
    calculate_orbit(0.2, 1000, 'a')

