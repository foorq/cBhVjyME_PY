from c_utilities import try_again_message, clear_screen


# Text Analysis
def text_analysis():
    print("Counting words, characters, and sentences in a given text.\n")

    while True:
        print("Please enter a string of words (Enter 'back' to return to the main menu):")
        ta_input = input("> ").strip().lower()
        if ta_input == 'back':
            return

        # Counting words by splitting the text by spaces
        num_words = len(ta_input.split())
        # Counting characters (including spaces and punctuation)
        num_chars = len(ta_input)

        # Counting sentences by splitting the text using common sentence endings
        num_sentences = []
        for end in ['.', '!', '?']:
            num_sentences.append(ta_input.count(end))
        num_sentences = sum(num_sentences)  # Find the sum because there are multiple endings

        print(f"\nNumber of words: {num_words}\nNumber of characters: {num_chars}\nNumber of sentences: {num_sentences}")
        try_again = try_again_message()
        if not try_again:
            return


# Fizz Buzz
def fizz_buzz():
    print("Counting upwards, from and to numbers of your choice: if a number is divisible by 3, 'Fizz' is generated "
          "instead of the number. If a number is divisible by 5, 'Buzz' is generated. Finally, if a number is divisible "
          "by both 3 and 5, 'Fizz Buzz' is generated.\n")

    while True:
        # Asks the user to input the starting number for the sequence
        print("Please enter a starting number (Enter 'back' to return to the main menu):")
        fb_input = input("> ").strip()

        if fb_input.lower() == 'back':
            return

        try:
            starting_num = int(fb_input)
            print("\nPlease enter the ending number:")
            ending_num = int(input("> "))  # Asks the user to input the ending number for the sequence
            clear_screen()

            if starting_num > ending_num:
                print("Output:\nNothing. Your starting number is > ending number: it should be the other way around.\n")
            else:
                print("Output:")
                for num in range(starting_num, ending_num + 1):
                    if (num % 3 == 0) and (num % 5 == 0):
                        print("Fizz Buzz")  # Print "Fizz Buzz" if the number is a multiple of both 3 and 5
                    elif num % 3 == 0:
                        print("Fizz")  # Print "Fizz" if the number is a multiple of 3
                    elif num % 5 == 0:
                        print("Buzz")  # Print "Buzz" if the number is a multiple of 3
                    else:
                        print(num)  # Otherwise, just print the number

                try_again = try_again_message()
                if not try_again:
                    # If the user chooses 'N', menu_prompt is displayed
                    return

        except ValueError:
            print("\nThat is not a valid number!")


# Palindrome Check
def palindrome_check():
    print("A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward. "
          "Basically, it remains unchanged when read from left to right and right to left.\n")

    while True:
        print("Please enter a word that could be a palindrome (Enter 'back' to return to the main menu):")
        pd_input = input("> ").strip()

        if pd_input.lower() == 'back':
            return

        # If the user's input is the same forward as it is reversed, it is a palindrome - otherwise, it is not
        if list(pd_input.lower()) == list(reversed(pd_input.lower())):
            print(f"\n{pd_input.capitalize()} is a palindrome.")
        else:
            print(f"\n{pd_input.capitalize()} is not a palindrome.")
        try_again = try_again_message()
        if not try_again:
            return


def pl_setting_up(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = text.split()
    pig_latin_words = []

    for word in words:
        # If the first letter is a vowel, add 'way' to the end
        if word[0].lower() in vowels:
            pig_latin_words.append(word + 'way')
        else:
            # Otherwise, find the point where there is a vowel (index += 1 until it reaches a vowel and breaks)
            index = 0
            for element in word:
                if element.lower() in vowels:
                    break
                else:
                    index += 1
            # Result: the part of the word starting from the vowel + the part before the vowel + 'ay'
            pig_latin_words.append(word[index:] + word[:index] + 'ay')
    return ' '.join(pig_latin_words)  # The translated words are now joined together into a single string separated by a space


# Pig Latin Translation
def pig_latin_translation():
    print("The rules of Pig Latin are as follows:\nFor words that begin with consonant sounds, take the first consonant "
          "or consonant cluster of the word and move it to the end of the word. Add 'ay' to the end of the word.\nFor words "
          "that begin with vowel sounds, simply add 'way' at the end of the word.\n")

    while True:
        print("Please enter a sentence to translate to Pig Latin (Enter 'back' to return to the main menu):")
        pl_input = input("> ").strip()

        if pl_input.lower() == 'back':
            return

        print(f"\nTranslated: {pl_setting_up(pl_input).capitalize()}.")  # We can now use pl_setting_up() for the user's input
        try_again = try_again_message()
        if not try_again:
            return


# Anagram Detection
def anagram_detection():
    print("An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original "
          "letters exactly once.\n")

    while True:
        print("Please enter your first word (Enter 'back' to return to the main menu):")
        first_word = input("> ").strip().lower()  # Strip any whitespaces and convert the string to lowercase

        if first_word == 'back':
            return

        print("\nPlease enter your second word:")
        second_word = input("> ").strip().lower()

        # The logic is: if the 2 strings are anagrams, they should produce the same letters when sorted
        if sorted(first_word) == sorted(second_word):
            print(f"\n{first_word.capitalize()} and {second_word} are anagrams.")
        else:
            print(f"\n{first_word.capitalize()} and {second_word} are not anagrams.")

        try_again = try_again_message()
        if not try_again:
            return


# Caesar Cipher Encryption
def caesar_cipher(text, shift):
    encrypted_text = ""
    shift %= 26  # If 'shift' > 25 or < 0, '%=' helps bring it within the valid range by dividing it by 26 and taking the remainder

    # The idea is to convert the alphabets to numbers first, add the shift amount, determine if the numbers > 25 or < 0, and then convert them back to letters
    for character in text:
        if character.isalpha():  # Check if the character is a letter
            # Shifts a single character by the given amount and returns the corresponding integer
            shifted = ord(character) + shift

            if character.islower():  # Handling lowercase letters
                # Add or subtract 26; otherwise, the shift will go beyond the end of the alphabet
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26

            else:  # Handling uppercase letters
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)  # Takes an integer and returns the corresponding character
        else:
            encrypted_text += character  # Non-alphabetic characters remain unchanged
    return encrypted_text


def caesar_cipher_encryption():
    print("The Caesar Cipher is a substitution cipher where each letter is shifted a certain number of places up or down "
          "the alphabet. Non-alphabetic characters remain unchanged.\n")

    while True:
        print("What message do you wish to encrypt? (Enter 'back' to return to the main menu):")
        cce_input = input("> ").strip()

        if cce_input.lower() == 'back':
            return

        print("\nPlease enter the shift amount (positive for right shift, negative for left shift):")
        shift_amount = input("> ").strip()

        try:
            # We can now use caesar_cipher() for the user's input
            shift_amount = int(shift_amount)  # Convert input to integer for the shift
            print(f"\nEncrypted message: {caesar_cipher(cce_input, shift_amount)}")

            try_again = try_again_message()
            if not try_again:
                return

        except ValueError:
            print("\nThat is not a valid number!")


# Letter Pattern Recognition
def letter_pattern_recognition():
    print("Checking for repeated substrings within a given string.\n")

    while True:
        print("Please enter a string of words (Enter 'back' to return to the main menu):")
        lpr_input = input("> ").strip().lower()
        if lpr_input == 'back':
            return

        patterns = set()  # Initialise an empty set to store identified patterns
        max_pattern_length = len(lpr_input) // 2  # Define the maximum length of a pattern (maximum half of the text length)

        # Iterate through possible pattern lengths from 1 to max_pattern_length
        for pattern_length in range(1, max_pattern_length + 1):

            # Make sure there is enough remaining text for both the current pattern and the next one to be compared for repetition
            for i in range(len(lpr_input) - pattern_length):
                # Extract 2 substrings of the current pattern length
                pattern = lpr_input[i:i + pattern_length]  # Substring

                # Check if the current pattern appears again in the text
                if lpr_input.count(pattern) >= 2:
                    patterns.add(pattern)

        if patterns:
            print(f"\nSubstrings that appear multiple times within the text: {', '.join(patterns)}.")
        else:
            print("\nNo repeated substrings found in the text.")

        try_again = try_again_message()
        if not try_again:
            return
