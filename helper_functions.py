def validate_input(user_input):
    # Check if the input is a non-empty string
    if isinstance(user_input, str) and user_input.strip()!="":
        return True
    else:
        return False
        
def convert_to_binary(text):
     # Convert text to binary 
     if str(text) .isdigit():
        return bin(int(text))
     else:
         return ' '.join(format(ord(char), '08b') for char in text )

    
def create_message(name, age, name_binary, age_binary):
    # Create a  message
    return(
        f"hello {name}, your age {age} years old.\n"
        f"Name in binary: {name_binary}\n"
        f"Age in binary: {age_binary}"
    )
 
    
