# Morse Code Converter

## Description
This is a simple text-based (command-line) Python program that converts any string input into Morse code. It follows the standard Morse code representation for letters and numbers, separating Morse code symbols with spaces and words with a forward slash (`/`).

## Features
- Converts alphanumeric text input to Morse code
- Case-insensitive conversion (all input is converted to uppercase)
- Spaces between words are replaced with a `/` symbol
- Provides a dictionary mapping letters and numbers to Morse code

## How It Works
The program follows these steps:
1. Creates a dictionary that maps letters and numbers to their Morse code equivalents.
2. Takes user input and converts it to uppercase for consistency.
3. Replaces each character in the string with its corresponding Morse code.
4. Separates Morse code symbols with spaces and words with a forward slash (`/`).

## Installation & Usage
### Prerequisites
- Python 3.x installed

### Running the Program
1. Clone this repository or copy the script.
2. Open a terminal and navigate to the script's location.
3. Run the script using:
   ```bash
   python morse_code_converter.py
   ```
4. Enter a string when prompted.
5. The program will output the Morse code equivalent of your input.

## Code Example
### Morse Code Dictionary
```python
MORSE_CODE_DICT = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..",
    "9": "----.", " ": "/"  # Space between words is represented by "/"
}
```

### Conversion Function
```python
def text_to_morse_code(input_texts):
    morse_code = []  # Initialize the list to store Morse code translations
    for letter in input_texts.upper():  # Convert input to uppercase for consistency
        if letter in MORSE_CODE_DICT:  # Check if the letter exists in dictionary
            morse_code.append(MORSE_CODE_DICT[letter])
    return ' '.join(morse_code)  # Return Morse code as a string
```

### Example Usage
```python
input_text = input("Please enter a string: ")
result = text_to_morse_code(input_text)
print(f'The Morse code for "{input_text}" is: {result}')
```

### Sample Output
```
Please enter a string: Hello World
The Morse code for "Hello World" is: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

## License
This project is open-source and available for modification and redistribution.

## Author
Mei Zhang

