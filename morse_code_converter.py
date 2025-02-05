# Copyright (c) 2025 [Mei Zhang]
# All rights reserved.
# This software is licensed under the MIT License (or another license of your choice).


# Create a text-based (command line) program that takes any String input and converts it into Morse Code.

# -------------------------------Steps:----------------------------------------------
# 1. Create a dictionary that maps letters and numbers to Morse code.
# 2. Take an input string and convert it to uppercase (Morse code is case-insensitive).
# 3. Replace each character in the string with its Morse code equivalent.
# 4. Separate Morse code symbols with spaces and words with a forward slash (/).


# 1. Create a dictionary that maps letters and numbers to Morse code.
MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/",  # Space between words is represented by "/"
}


# 2. Take an input string and convert it to uppercase (Morse code is case-insensitive).
input_text = input("Please enter a string: ")
# print(f"check input_value: {input_text}")


# 3. Replace each character in the string with its Morse code equivalent.
# Check each letter of the input_value against KEY of MORSE_CODE_DICT
# If match then take its Value.


def text_to_morse_code(input_texts):
    morse_code = []  # Initialize the list to store Morse code translations
    for letter in input_texts.upper():  # Convert input to uppercase for consistency
        if letter in MORSE_CODE_DICT:  # Check if the letter exists in dictionary
            morse_code.append(MORSE_CODE_DICT[letter])

    return morse_code  # Return the Morse code list


# Example Usage
result = text_to_morse_code(input_text)
# print("Morse Code List:", result)
print(f'The morse code for "{input_text}" is \n {" ".join(result)}')
