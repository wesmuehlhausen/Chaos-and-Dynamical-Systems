import math
from decimal import *

class C():
    def run(self):
        print("Hello")

    def NewtonsMethod(self, input, guess, tolerance):

        # Error Checking
        print("__NEWTON_METHOD_SQUARE_ROOT_CALCULATOR_______________________________________________")
        if input < 0 or guess < 0 or tolerance < 0:
            print(f'Error: negative numbers are not valid inputs')
            return
        elif input == 0 or guess == 0 or tolerance == 0:
            print(f'Error: 0 is not a valid input')
            return
        else:
            print(f'Calculating Sqrt({input}) with the Guess: {guess} and error of 10^- {tolerance}')

        # Initialize Variables
        root = guess
        function_completed = False
        i = 1

        # Loop until hit accuracy
        while function_completed == False:
            # Newtons Equation
            root = 0.5 * (root + (input / root))

            # Pretty Print
            formatted_root = "{:.25f}".format(root)
            if root < 10 and i < 10: #Check to see if less than 10
                print(f' {i})  {formatted_root}')
            elif (root >= 10 and i < 10):
                print(f' {i}) {formatted_root}')
            elif (i >= 10 and root < 10):
                print(f'{i})  {formatted_root}')
            else:  # Assume number is greater than 10
                print(f'{i}) {formatted_root}')
            # Increment Iteration
            i += 1

            # Check if calculated is within error of actual value
            if (abs(math.sqrt(input)-root) < (10**(tolerance*(-1)))):
                # Print out where the tolerance level is
                marker = "      "
                for x in range(tolerance):
                    marker += " "
                marker += "^"
                print(marker)

                # Print out computer calculated square root
                function_completed = True
                if root >= 10:
                    print("REAL " + "{:.25f}".format(math.sqrt(input)))
                else:
                    print("REAL " + "{:.25f}".format(math.sqrt(input)))
                print(" ")
                print(" ")

# Run here!
if __name__ == '__main__':
    C().NewtonsMethod(11, 100, 5)
    C().NewtonsMethod(11, 100, 10)
    C().NewtonsMethod(11, 100, 20)
    C().NewtonsMethod(-4, 100, 10)