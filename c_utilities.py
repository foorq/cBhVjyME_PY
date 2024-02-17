import os


def clear_screen():
    # Clears screen regardless of user's operating system
    if os.name == 'nt':  # 'nt' = Windows os
        os.system('cls')
    else:  # Covers every other os
        os.system('clear')


def try_again_message():
    # Function to handle user input for trying the same operation again (or not)
    while True:
        ta_input = input("\nTry again? (Y/N) > ").strip()
        if ta_input.upper() == 'Y':
            clear_screen()
            return True
        elif ta_input.upper() == 'N':
            return False
        else:
            print("Please enter 'Y' or 'N' only!")
