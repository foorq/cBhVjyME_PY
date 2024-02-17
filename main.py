from a_math import sum_multiples_3_5, lattice_paths, collatz_sequence, pascals_triangle, happy_number, armstrong_number, fibonacci_sequence
from b_language import text_analysis, fizz_buzz, palindrome_check, pig_latin_translation, anagram_detection, caesar_cipher_encryption, letter_pattern_recognition
from c_utilities import clear_screen
from colorama import init, Fore, Style

init()  # Initialise colorama
menu_prompt = f"""Hello. In this project, I am experimenting with Python to explore math and language-related concepts. I started this because I noticed that, while these concepts can be solved manually, tackling them in code requires a different way of thinking!

{Style.BRIGHT}Math-Related Concepts:{Style.RESET_ALL}
{Fore.RED}1.{Fore.RESET} Sum of Multiples of 3 or 5
{Fore.RED}2.{Fore.RESET} Lattice Paths
{Fore.RED}3.{Fore.RESET} Collatz Sequence
{Fore.RED}4.{Fore.RESET} Pascal's Triangle
{Fore.RED}5.{Fore.RESET} Happy Number
{Fore.RED}6.{Fore.RESET} Armstrong Number
{Fore.RED}7.{Fore.RESET} Fibonacci Sequence

{Style.BRIGHT}Language-Related Concepts:{Style.RESET_ALL}
{Fore.RED}8.{Fore.RESET} Text Analysis
{Fore.RED}9.{Fore.RESET} Fizz Buzz
{Fore.RED}10.{Fore.RESET} Palindrome Check
{Fore.RED}11.{Fore.RESET} Pig Latin Translation
{Fore.RED}12.{Fore.RESET} Anagram Detection
{Fore.RED}13.{Fore.RESET} Caesar Cipher Encryption
{Fore.RED}14.{Fore.RESET} Letter Pattern Recognition

Please select an option (or type 'exit' to quit). The explanations for each one are within:"""


def main_menu():
    show_menu = True
    while True:
        if show_menu:  # Display the main menu when show_menu is True
            clear_screen()  # Clear the screen to prevent clogging
            print(menu_prompt)
        user_selection = input("> ").strip()

        if user_selection.lower() == 'exit':
            exit(0)

        # Define a dictionary mapping user selections to function names
        selection_to_function = {
            '1': ('Sum of Multiples of 3 or 5', sum_multiples_3_5),
            '2': ('Lattice Paths', lattice_paths),
            '3': ('Collatz Sequence', collatz_sequence),
            '4': ("Pascal's Triangle", pascals_triangle),
            '5': ('Happy Number', happy_number),
            '6': ('Armstrong Number', armstrong_number),
            '7': ('Fibonacci Sequence', fibonacci_sequence),
            '8': ('Text Analysis', text_analysis),
            '9': ('Fizz Buzz', fizz_buzz),
            '10': ('Palindrome Check', palindrome_check),
            '11': ('Pig Latin Translation', pig_latin_translation),
            '12': ('Anagram Detection', anagram_detection),
            '13': ('Caesar Cipher Encryption', caesar_cipher_encryption),
            '14': ('Letter Pattern Recognition', letter_pattern_recognition)
        }

        # Check if user selection is in the dictionary keys
        if user_selection in selection_to_function:
            clear_screen()

            # Get the function name and description from the dictionary
            function_name, function = selection_to_function[user_selection]
            print(f"{Fore.RED}You have chosen '{function_name}'.{Fore.RESET}")

            # Call the selected function
            function()
            show_menu = True  # Reset flag to display the main menu again

        else:
            print("\nInvalid option! Please choose a number from 1 to 15 or input 'exit'.")
            show_menu = False  # Keep the menu hidden after an invalid option


if __name__ == '__main__':
    # Function runs only when the script is executed as the main program
    main_menu()
