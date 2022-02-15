import matplotlib.pyplot as plt
import numpy as np


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def calculate_orbit(name, c_left, c_right, c_incriment, loop_count, seed):
    print(f"Calculating Orbit of {seed}")

    # Main Loop for each c value
    c = c_right

    while c >= c_left:

        # For the given value of c (which is i) and initialize arrays
        x = seed
        x_array = []
        c_array = []
        for i in range(loop_count):

            #  Normal Case, Plug and update
            try:
                # print(f"Iteration {i} of [c = {c}] = {x}")
                x = (x ** 2) + c
            except:
                print("Infinite value found")
            else:
                #  x = y  # update x value
                x_array += [x]  # Fill up and array and evaluate for cycle


        tmp_array = []
        for j in reversed(range(len(x_array))):
            tmp = round(x_array[j], 4)
            if tmp in tmp_array:
                # print(f"Duplicate of {tmp} found on iteration {j}")
                break
            else:
                tmp_array += [tmp]
                c_array += [c]
        plt.plot(c_array, tmp_array, color='green', linestyle='none', linewidth=3,
                 marker='o', markerfacecolor='blue', markersize=.1)


        # Incriment
        # print(tmp_array)
        c -= c_incriment
        c = round(c, 3)

        # Print Values
        # print(f'C: {c} -> {x_array}')

    plt.title(f'{name}   |   Seed = {seed}   |   Iterations = {loop_count} (per C value)')
    plt.xlim(c_left, c_right)
    plt.ylim(-2, 2)
    plt.xlabel('C values')
    plt.ylabel('X values')
    # plt.legend()
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate_orbit("Q(x) = x^2 + c",
                    -2, 0.25, 0.001,  # C value range and increment
                    10000, 0)  # Loop count and seed

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
