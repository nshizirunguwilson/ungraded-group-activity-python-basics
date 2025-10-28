def validate_input(user_input):
    # check if input is not empty and is a string
    if isinstance(user_input, str) and user_input.strip() != "":
        return True
    else:
        return False

def convert_to_binary(text):
    # Converts any string (e.g., a name) into its binary form using ASCII values. Example: "Hi" → "01001000 01101001"
    # If the input is a number (like age), convert it to an integer and then to binary using bin().
    if text.isdigit():
        # return bin(int(text))[2:]  # Convert number to binary and remove '0b' prefix
        return bin(int(text))  # Convert number to binary
    else:
        return ' '.join(format(ord(char), '08b') for char in text)  # Convert each character to binary

# testing the function to convert input to binary
# value = input("Enter your name or age: ")
# output = convert_to_binary(value)
# print(f"Binary representation: {output}")

def create_message(name, age, name_binary, age_binary):
    return (
        f"Hello, {name}, you are {age} years old.\n"
        f"Name in binary: {name_binary}\n"
        f"Age in binary: {age_binary}"
    )
