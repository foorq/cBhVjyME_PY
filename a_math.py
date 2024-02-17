from c_utilities import try_again_message, clear_screen
import math


# Sum of Multiples of 3 or 5
def multiples(number):
    sum_multiples = 0
    for num in range(number):
        # Take note of numbers that are both multiples of 3 and 5 (avoid repetition)
        if (num % 3 == 0 and num % 5 == 0) or num % 3 == 0 or num % 5 == 0:
            sum_multiples += num
    return sum_multiples


def sum_multiples_3_5():
    print("I will find the sum of all the multiples of 3 or 5 below a number that you specify.\n")

    while True:
        print("Please enter a number (Enter 'back' to return to the main menu):")
        m35_input = input("> ").strip()

        if m35_input.lower() == 'back':
            return

        try:
            if int(m35_input) > 0:  # Check if it's a valid positive number
                print(f"\nThe total sum of the multiples below {int(m35_input):,} is: {multiples(int(m35_input)):,}.")

                try_again = try_again_message()
                if not try_again:
                    return

            else:
                print("\nYour number must be positive!")

        except ValueError:
            print(f"\nThat is not a valid number!")


# Lattice Paths
def lattice_paths():
    print("In a grid, a lattice path refers to a path that moves from the top-left corner to the bottom-right corner by "
          "only moving right or down, along the grid lines.\n\nFor example, in a 2x2 grid, there are 6 possible lattice "
          "paths:\nRight > Down > Right > Down\nRight > Right > Down > Down\nDown > Right > Right > Down\nDown > Down > Right "
          "> Right\nRight > Down > Down > Right\nDown > Right > Down > Right\n")

    # In a grid, the number of lattice paths is found using the formula (n + m) C n
    # (n + m) represents the number of steps we need to take down and to the right
    while True:
        print("Please enter the number of rows you want in a grid (Enter 'back' to return to the main menu):")
        lp_row = input("> ").strip()

        if lp_row.lower() == 'back':
            return

        try:
            lp_row = int(lp_row)
            print("\nPlease enter the number of columns:")
            lp_column = int(input("> "))

            # lp_row, lp_column is lp_row C lp_column
            print(f"\nThere are {math.comb(lp_row + lp_column, lp_column):,} possible lattice paths in a {lp_row}x{lp_column} grid.")

            try_again = try_again_message()
            if not try_again:
                return

        except ValueError:
            print("\nThat is not a valid number!")


# Collatz Sequence
def collatz_sequence():
    print("The Collatz sequence operates by the following rules:\n\nStart with any positive integer, denoted as 'n':\n"
          "If 'n' is even, divide it by 2.\nIf 'n' is odd, multiply it by 3 and add 1.\nRepeat the process with the resulting "
          "number, continuing until the sequence reaches the number 1.\n")

    while True:
        print("Please enter the starting number (Enter 'back' to return to the main menu):")
        cs_input = input("> ").strip()
        if cs_input.lower() == 'back':
            return

        try:
            cs_input = int(cs_input)
            if cs_input <= 0:  # Check if the input is positive
                print("\nYour number must be positive!")
                continue  # Restart the loop if the input is not positive

            sequence = [cs_input]

            # Keep iterating until the number is 1
            while cs_input != 1:
                # If the number is divisible by 2, i.e. even, divide it by 2; else, multiply it by 3 and add 1
                if cs_input % 2 == 0:
                    cs_input //= 2
                else:
                    cs_input = (cs_input * 3) + 1

                sequence.append(cs_input)  # Append the next number to the sequence

            new_sequence = '\n'.join(map(str, sequence))
            clear_screen()
            print(f"The sequence starting from {sequence[0]} is: \n{new_sequence}")
            try_again = try_again_message()
            if not try_again:
                return

        except ValueError:
            print("\nThat is not a valid number!")


# Pascal's Triangle
def pascals_triangle_display(rows):
    # List to store the rows
    triangle = []

    for row_num in range(rows):
        # Initialise each row with 1s
        row = [1] * (row_num + 1)

        # Calculate elements in the row (excluding the ends)
        for j in range(1, row_num):
            # Calculate each element by summing the 2 elements from the row above
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
        triangle.append(row)

    # List to store the centered display-ready rows
    display = []
    max_width = len(" ".join(map(str, triangle[-1])))  # Calculate the width of the last row

    for row in triangle:
        row_string = " ".join(map(str, row))  # Convert row elements to string and join with spaces
        row_width = len(row_string)  # Calculate the width of the current row
        left_padding = (max_width - row_width) // 2  # Calculate left padding to center-align the row

        # Create the row for display by adding left padding
        row_display = " " * left_padding + row_string
        display.append(row_display)

    return display


def pascals_triangle():
    print("Pascal's Triangle is a triangular array of numbers that is constructed as follows:\nThe topmost row contains "
          "only the number 1.\nEach subsequent row is constructed by placing 1s on both ends.\nTo generate the numbers "
          "inside each row, add the two numbers directly above to determine the number in the current position.")
    print("""
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
""")

    while True:
        print("Please enter the number of rows you would like to see in Pascal's Triangle (Enter 'back' to return to the main menu):")
        pt_input = input("> ").strip()

        if pt_input.lower() == 'back':
            return

        try:
            pt_input = int(pt_input)
            if pt_input <= 0:
                print("\nYour number must be positive!")
                continue

            p_triangle = pascals_triangle_display(pt_input)
            print(f"\nPascal's Triangle with {pt_input} rows:")
            for row in p_triangle:
                print(row)  # Print each centered row from the list

            try_again = try_again_message()
            if not try_again:
                return

        except ValueError:
            print("\nThat is not a valid number!")


# Happy Number
def is_happy_number(n):
    seen = set()  # Initialise an empty set to store numbers encountered during the process

    # While n is not = 1 and not seen in the cycle, calculate the sum of the squared digits of n
    while n != 1 and n not in seen:
        seen.add(n)
        n_digits_squared = []
        for d in str(n):
            n_digits_squared.append(int(d)**2)
        n = sum(n_digits_squared)

    return n == 1  # If n = 1, i.e. True, the number is a happy number; otherwise, it returns False


def happy_number():
    print("A happy number is a special type of number that, when you repeatedly replace the number by the sum of the "
          "squares of its digits, eventually reaches the number 1.\n\nFor example, taking the number 19:\n1^2 + 9^2 = 1 "
          "+ 81 = 82\n8^2 + 2^2 = 64 + 4 = 68\n6^2 + 8^2 = 36 + 64 = 100\n1^2 + 0^2 = 1 + 0 = 1\n\nTherefore, 19 is a "
          "happy number.\n")

    while True:
        print("Please enter a number to check if it is a happy number (Enter 'back' to return to the main menu):")
        hn_input = input("> ").strip()
        if hn_input.lower() == 'back':
            return

        try:
            number = int(hn_input)
            if is_happy_number(number):
                print(f"\n{number} is a happy number.")
            else:
                print(f"\n{number} is not a happy number.")

            try_again = try_again_message()
            if not try_again:
                return

        except ValueError:
            print("\nThat is not a valid number!")


# Armstrong Number
def armstrong_number():
    print("An Armstrong number is equal to the sum of its own digits, each raised to the power of the number of digits."
          "\n\nFor example, taking the number 153:\nIt has 3 digits: 1, 5, and 3. Hence, each digit is raised to the power "
          "of 3.\n1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153\n\nTherefore, 153 is an Armstrong number.\n")

    while True:
        print("Please enter a number to check if it is an Armstrong number (Enter 'back' to return to the main menu):")
        an_input = input("> ").strip()
        if an_input.lower() == 'back':
            return

        try:
            # Append each digit into the digits_list to find the length/number of digits
            digits_list = []
            for d in an_input:
                digits_list.append(int(d))

            no_of_digits = len(digits_list)
            # Bring each digit in the digits_list to the power of the number of digits
            armstrong_check = sum(int(digit) ** no_of_digits for digit in digits_list)

            # If the sum of the digits ** number of digits = the original number (that the user input), it is an Armstrong number
            if armstrong_check == int(an_input):
                print(f"\n{an_input} is an Armstrong number.")
            else:
                print(f"\n{an_input} is not an Armstrong number.")

            try_again = try_again_message()
            if not try_again:
                return

        except ValueError:
            print("\nThat is not a valid number!")


# Fibonacci Sequence
def fibonacci(n):  # Function to generate the sequence up to 'n' terms
    sequence = []
    a, b = 0, 1  # Initial numbers in the sequence are 0 and 1
    for _ in range(n):
        sequence.append(a)  # Append 0 first, then 1, and then a sum of the 2 preceding numbers - so on and so forth
        a, b = b, a + b  # Shift the numbers: a = b, and b = sum of a and b
    return sequence


def fibonacci_sequence():
    print("A Fibonacci sequence is a series of numbers where each number is the sum of the 2 preceding ones, usually starting with 0 and 1.\n")
    while True:
        try:
            print("How many terms do you wish to generate? (Enter 'back' to return to the main menu):")
            fs_input = input("> ").strip()
            if fs_input.lower() == 'back':
                return

            clear_screen()
            fs_input = int(fs_input)
            sequence = '\n'.join(str(num) for num in fibonacci(fs_input))  # Necessary because Python version 3.11 does not allow backslashes inside expression parts of f-strings
            print(f"The Fibonacci sequence up to the first {fs_input} terms is:\n{sequence}")

            try_again = try_again_message()
            if not try_again:
                return

        except ValueError:
            print("That is not a valid number!")
