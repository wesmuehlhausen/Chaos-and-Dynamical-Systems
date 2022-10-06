import matplotlib.pyplot as plt
import numpy as np


# Function used to recursively plot a canter's middle third set
def middle_third(left, right, cur, n):
    x = []
    y = []
    i = left

    # Plot points every one thousandth
    while i < right:
        x += [i]
        y += [cur]
        i += 0.001

    # Plot the data
    plt.plot(x, y, color='green', linestyle='none', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=.5)

    # If we hit the set limit, do not continue the recursion
    if cur >= n:
        return
    # If we are under the limit of iterations, continue recursion
    else:
        cur += 1
        new13 = left + ((right - left) * (1 / 3))
        new23 = left + ((right - left) * (2 / 3))
        # print(f'(<{cur}>[{left},{new13}][{new23},{right}])')
        # Recursively iterate deeper into the canter set. Every range creates two more defined within its bounds
        middle_third(left, new13, cur, n)
        middle_third(new23, right, cur, n)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 10  # this is n in the equations. How many iterations we go deep
    middle_third(0, 1, 0, n)

    plt.title(f'F^n where n->{n}')
    plt.xlim(0, 1)
    plt.ylim(0, n)
    plt.xlabel('X Range')
    plt.ylabel('Iteration')
    # plt.legend()
    plt.show()

