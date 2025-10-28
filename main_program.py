#!/usr/bin/env python3

from helper_functions import validate_input, convert_to_binary, create_message
from greetings import show_intro, show_exit_message
from file_manager import save_message, read_message

def get_user_info():
    while True:
        name = input("Enter your name: ")
        if not validate_input(name):
            print("Invalid name! Please try again.")
            continue
        age = input("Enter your age: ")
        if not validate_input(age) or not age.isdigit():
            print("Invalid age! Please enter a number.")
            continue
        
        return name, age
    

if __name__ == "__main__":
    print(show_intro())
    name, age = get_user_info()
    name_binary = convert_to_binary(name)
    age_binary = convert_to_binary(age)
    message = create_message(name, age, name_binary, age_binary)
    print(message)
    save_message(message)
    read_message()
    print(show_exit_message())