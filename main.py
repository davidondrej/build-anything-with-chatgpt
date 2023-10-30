# Morse Code Translator

# Step 1: Dictionary for morse code
english_to_morse = {
    # Alphabets
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..',

    # Numbers
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.',

    # Special Characters
    '.': '.-.-.-',  # Period
    ',': '--..--',  # Comma
    '?': '..--..',  # Question mark
    "'": '.----.',  # Single quotation mark (apostrophe)
    '!': '-.-.--',  # Exclamation mark (Note: This is an unofficial code, but is commonly used.)
    '/': '-..-.',   # Forward slash
    '(': '-.--.',   # Open parenthesis (or bracket)
    ')': '-.--.-',  # Close parenthesis (or bracket)
    '&': '.-...',   # Ampersand
    ':': '---...',  # Colon
    ';': '-.-.-.',  # Semicolon
    '=': '-...-',   # Equals sign
    '+': '.-.-.',   # Plus sign
    '-': '-....-',  # Hyphen or minus sign
    '_': '..--.-',  # Underscore
    '"': '.-..-.',  # Double quotation mark
    '$': '...-..-', # Dollar sign (Note: This is also an unofficial code but is sometimes used.)
    '@': '.--.-.',  # At symbol (Note: This is an unofficial code but is often used.)
    
}


# Step 2: Get user input
user_string = input("Enter a random English text: ")


# Step 3: Write a function to translate the text based on user choice.
def translate(text):
    # convert text to consistent case
    text = text.upper()
    # initialize an empty string for the Morse code result
    morse_string = ""
    # loop through each character in the text
    
    for char in text:
        # update the morse_string with the morse code for the character
        try:
            if char == " ":
                morse_string += "  "
            else:
                morse_string += english_to_morse[char] + " "
        except KeyError:
            print("Sorry, I can't translate this character: " + char)
            morse_string += char + " "

    
    # make the function give back the new morse_string
    return morse_string


# Step 4: Show the translated text to the user
print(translate(user_string))
