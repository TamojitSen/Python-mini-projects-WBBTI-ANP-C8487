#program to determine the type of character entered by the user
char = input("Enter a single character: ")
    
# Ensure the input is a single character
if len(char) != 1:
    print("Please enter exactly one character.")

# Get the ASCII value of the character
ascii_value = ord(char)

# Determine the type of character based on ASCII values
if 65 <= ascii_value <= 90:  # ASCII range for 'A' to 'Z'
    print(f"The character '{char}' is a capital letter.")
elif 97 <= ascii_value <= 122:  # ASCII range for 'a' to 'z'
    print(f"The character '{char}' is a lowercase letter.")
elif 48 <= ascii_value <= 57:  # ASCII range for '0' to '9'
    print(f"The character '{char}' is a digit.")
else:  # Any other character
    print(f"The character '{char}' is a special symbol.")