def save_message(message):
    try:
        with open("message.txt", "w") as file:
            file.write(message)
        print("Message saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving the message: {e}")

def read_message():
    print("Reading saved message...")
    try:
        with open("message.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No saved message found.")
    except Exception as e:
        print(f"An error occurred while reading the message: {e}")


# must save message.txt in same directory as this file
# must append new information not to delete the existing information