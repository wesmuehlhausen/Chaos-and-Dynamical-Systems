# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math


def individual_orbit(seed, loop_count):
    # Initialize varaibles
    count = 1  # count is 1
    x = seed
    max = 10 ** 150  # if a value is greater than this, we can assume it is infinity
    infinite = False
    print(x)
    print(seed)

    # For each x0 value, run loop_count times to see where the value goes
    for i in range(loop_count):
        try:  # Try to do the equation
            # y = x * math.sin(x)
            #  y = (x * x) - 1.1
            y = x * ((x ** 2) - 4)  # y = x((x^2)-4)
        except:  # if it causes an error, we assume the number is too big/small. I.E. +/- Infinity
            print("!!!")
            infinite = True
            break
        else:  # if the calculation worked
            x = y  # Reassign new seed value from result of previous solution
            # check to see if value still is too big and can be considered infinity
            if x > max or x < (max * -1):
                infinite = True
                break
            else:
                print(f'{count}) {x}')
                count += 1

    # Print out seed value with one decimal
    if infinite == True:
        print(f"Seed: {seed}  |  Result: Diverged to +/- infinity")
    else:
        print(f'Seed: {seed}  |  Result: Converged to {x}')
    print("_________________________________________________________")



def calculate_orbit(left_bound, right_bound, increment, loop_count):

    # Initialize varaibles
    count = 1  # count is 1
    x0 = left_bound  # set i to left bound
    max = 10 ** 150  # if a value is greater than this, we can assume it is infinity
    infinite = False
    pos_neg = 0

    # Iterate from left bound to right bound as x0 value
    while x0 <= right_bound:

        x0 = round(x0, 3)
        x = x0  # set variable x to seed value
        infinite = False

        # For each x0 value, run loop_count times to see where the value goes
        for i in range(loop_count):
            try:  # Try to do the equation
                # y = (1 / x)
                # y = x * math.sin(x)
                y = x * ((x ** 2) - 4)  # y = x((x^2)-4)
            except:  # if it causes an error, we assume the number is too big/small. I.E. +/- Infinity
                infinite = True
                break
            else:  # if the calculation worked
                x = y  # Reassign new seed value from result of previous solution
                # check to see if value still is too big and can be considered infinity
                if x > max or x < (max * -1):
                    if x > max:
                        pos_neg = 1
                    else:
                        pos_neg = -1
                    infinite = True
                    break

        # Print out seed value with one decimal
        if infinite == True:
            if pos_neg == 1:
                print(f"Seed: {x0}  |  Result: Diverged to +infinity")
            else:
                print(f"Seed: {x0}  |  Result: Diverged to -infinity")

        else:
            # copy = x0
            # formatted_copy = '{0:.2g}'.format(copy)
            print(f'Seed: {x0}  |  Result: Converged to {x}')
        x0 += increment  # increment loop
        count += 1

    print("\nProgram Info")
    print(f'\n>Equation:      y = x(x^2 - 4)'
          f'\n>Test range:    [{left_bound} --> {right_bound}] '
          f'\n>Iterations:    {increment} '
          f'\n>Loops:         {loop_count} loops'
          f'\n>Calculations:  {loop_count/increment*(right_bound-left_bound)}\n\n')
    print("Note: Use CTRL-F to search for 'Converged' to find points that didn't stray to infinity")





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate_orbit(-5, 5, 0.001, 1000)
    # individual_orbit(2.2361, 100)  # Uncomment this to test an individual seed
    # individual_orbit(2, 150)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
