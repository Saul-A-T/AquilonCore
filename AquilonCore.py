import string
memory = {}

def generate_response(command):

    clean_command = command.translate(
       str.maketrans("", "", string.punctuation)
    ).strip()

    words = clean_command.split()
    
    if command == "help":
      return (
        "Available commands:\n"
        "1. Help - Show available commands\n" 
        "2. Quit - Exit Aquilon Core\n" 
        "3. Hello/Hi/Hey - Greet Aquilon Core\n" 
        "4. Status - Check system status\n" 
        "5. Who are you - Get information about Aquilon Core\n"
        "6. My name is... - Tell Aquilon Core your name\n"
        "7. What is my name - Ask Aquilon for your name\n"
      )


    elif command.startswith("my name is "):
      name = command.replace("my name is ", "", 1).strip()

      if name:
          memory["name"] = name.title()
          return f"Nice to meet you, {memory['name']}!"

    elif "what" in words and "name" in words:
      if "name" in memory:
          return f"Your name is {memory['name']}."
      else:
          return "I don't know your name yet."

    elif any(word in words for word in ["hello", "hi", "hey"]):
      return "Greetings! How can I be of service?"

    elif "status" in words:
      return "All systems are operational.\nCore status - ONLINE"

    elif "who" in words and "are" in words and "you" in words:
      return "I am Aquilon Core, a Python-based chatbot"

    else: return "Message received"

print("Welcome to Aquilon Core")
print("Aquilon: How can I help you today?")

while True:
    user_input = input("You: ")
    command = user_input.lower()

    if command == "quit":
        print("Aquilon: Goodbye!")
        break

    response = generate_response(command)

    print(f"Aquilon: {response}")
