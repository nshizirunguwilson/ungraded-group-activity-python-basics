def validate_input(user_input):
    if isinstance(user_input, str) and user_input.strip()!="":
        return True
    else:
        return False
    
def create_message(name, age, name_binary, age_binary):
    return(
        f"hello {name}, your age {age} years old.\n"
        f"Name in binary: {name_binary}\n"
        f"Age in binary: {age_binary}"
    )
    

  
    