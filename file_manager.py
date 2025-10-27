def save_message(message):
  try:
    with open('user_message.txt', 'w', encoding='utf-8') as file:
        file.write(message)
        print("Message saved successfully.")

  except Exception as e:
        print(f" Error saving message: {e}")

def read_message():
    try:
        with open('user_message.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            print("The saved message is:")
            print(content)
    except FileNotFoundError:
        print("Error: The file 'user_message.txt' was not found.")
    except Exception as e:
        print(f" Error reading message: {e}")
