import matplotlib.pyplot as plt
import numpy as np

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def calculate_orbit(name, c_left, c_right, c_incriment, loop_count, seed):


    print("Calculating Orbit")

    # Main Loop for each c value
    c = c_left
    while c <= c_right:

        #For the given value of c (which is i)
        x = seed
        x_array = []
        c_array = []
        for i in range(loop_count):

            #  Normal Case, Plug and update
            try:
                y = x ** x + c
            except:
                print("Infinite value found")
            else:
                x = y  # update x value
                x_array += [x]  #  Fill up and array and evaluate for cycle
                c_array += [c]


        #  Plot the correct number of values
        # if at the last 10% of calculations, plot them
        if i > (loop_count - 100):
            plt.plot(c_array, x_array, color='green', linestyle='none', linewidth=3,
         marker='o', markerfacecolor='blue', markersize=1)





        # Incriment
        print(c)
        c += c_incriment
        c = round(c, 2)

    # Create the graph
    print(c_array)
    print(x_array)

    plt.title(f'{name}   |   Seed = {seed}   |   Iterations = {loop_count}')
    plt.xlim(-2, 0.25)
    plt.ylim(-2, -2)
    plt.xlabel('C values')
    plt.ylabel('X values')
    plt.legend()
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate_orbit("Q(x) = x^2 + c",
                    -2, 0.25, 0.1,  # C value range and increment
                    1000, 0)  # Loop count and seed

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
