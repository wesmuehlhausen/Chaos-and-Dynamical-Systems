import matplotlib.pyplot as plt
import numpy as np

def generate_point(equation_number, input):
    if equation_number == 'a':
        return 2.6 * input * (1 - input)
    elif  equation_number == 'b':
        return (-0.25 * input ** 3) + (-1.5 * input ** 2) + 1
    else:
        print(f"No equation selected for [Equation {equation_number}][Input: {input}]")

    return

def generate_points(x_values, y_values, seed, loop_count, equation_number):
    # x += [.2]
    # y += [.2]

    x = seed # initialize x value to seed value
    for i in range(loop_count):
        # Add point for where it hits F(x)
        x_values += [x]
        y_values += [x]

        # Get new point for L(x) and add points "L(x) = 2.6x(1-x)"
        y = generate_point(equation_number, x)
        x_values += [x]
        y_values += [y]
        x = y

def generate_cobweb(function, seed, loop_count, x_min, x_max, y_min, y_max, equation_number):

    # TODO Plot 0: Plot the Seed Value
    x0 = [seed]
    y0 = [seed]
    plt.plot(x0, y0, label="Seed", color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)

    #Plot 1: Calculated Values (The steps on the graph)
    x1 = []
    y1 = []
    generate_points(x1, y1, seed, loop_count, equation_number) # Make sure to add points to array
    print(x1)
    print(y1)
    plt.plot(x1, y1, label="C(x)")

    #Plot 2: Y = x
    x2 = [x_min, x_max]
    y2 = [y_min, y_max]
    plt.plot(x2, y2, label="F(x)")

    #Plot 3: Given Function
    x3 = np.arange(x_min, x_max, 0.001)

    y3 = 0
    if equation_number == 'a':
        y3 = (2.6 * x3) - (2.6 * x3 ** 2)
    elif equation_number == 'b':
        y3 = (-0.25 * (x3 ** 3)) + (-1.5 * (x3 ** 2)) + 1
    else:
        print("Error graphing given function")
    plt.plot(x3, y3, label="L(x)")

    #Create the Plot
    plt.title(f'{function}   |   Seed = {seed}   |   Iterations = {loop_count}')
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.legend()
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # generate_cobweb("L(x) = 2.6x(1-x)", 0.1, 25, 0, 1, 0, 1, 'a')
    # generate_cobweb("L(x) = 2.6x(1-x)", 0.4, 25, 0.37, 0.65, 0.37, 0.67, 'a')
    generate_cobweb("L(x) = .25x^3 - 1.5x^2 + 1", 0, 25, -1, 1.1, -2, 2, 'b')
    # generate_cobweb("L(x) = .25x^3 - 1.5x^2 + 1", -6, 10, -6, 2, -5, 2, 'b')


