import string

memory = {
    "name": None,
    "facts": []}

def generate_response(command):
    clean_command = command.translate(
        str.maketrans("", "", string.punctuation)
    ).strip()

    words = clean_command.split()
# Help
    if clean_command == "help":
        return (
            "Available commands:\n"
            "1. Help - Show available commands\n"
            "2. Quit - Exit Aquilon Core\n"
            "3. Hello/Hi/Hey - Greet Aquilon Core\n"
            "4. Status - Check system status\n"
            "5. Who are you - Get information about Aquilon Core\n"
            "6. My name is... - Tell Aquilon Core your name\n"
            "7. What is my name - Ask Aquilon for your name\n"
            "8. Remember that - Tell Aquilon to remember\n"
            "9. What do you remember - Check Aquilon core's memory\n"
            "10. Forget everything - Clear all stored memories\n"
            "11. Forget that - Clear specific memories\n"
            "12. Forget my name - Clear my name\n"
            "13. How are you - Ask Aquilon how it's doing"
        )
# Memory
    elif clean_command.startswith("remember that "):
        fact = clean_command.replace("remember that ", "", 1).strip()

        if fact:
            memory["facts"].append(fact)
            return f"I'll remember that: {fact}"
        else:
            return "What would you like me to remember?"

    elif "remember" in words or "memories" in words:
        if not memory["facts"]:
            return "I don't remember anything yet."
        else:
            return "I remember:\n- " + "\n- ".join(memory["facts"])

    elif clean_command == "forget everything":
        memory["facts"].clear()
        memory["name"] = None
        return "All memories have been cleared."

    elif clean_command == "forget my name":
        if not memory["name"]:
            return "I don't have your name stored."

        memory["name"] = None
        return "I have forgotten your name."

    elif clean_command.startswith("forget that"):
        fact = clean_command.replace("forget that", "", 1).strip()

        if not fact:
            return "What would you like me to forget?"

        if fact in memory["facts"]:
            memory["facts"].remove(fact)
            return f"I have forgotten that: {fact}"
        else:
            return "I don't remember that."

    elif clean_command.startswith("my name is "):
        name = clean_command.replace("my name is ", "", 1).strip()

        if name:
            memory["name"] = name.title()
            return f"Nice to meet you, {memory['name']}!"
# Answers
    elif "name" in words and (
        "what" in words or "whats" in words
        or "tell" in words or "know" in words
    ):
        if not memory["name"]:
            return "I don't know your name yet"
        else:
            return f"Your name is {memory['name']}."

    elif any(word in words for word in ["hello", "hi", "hey",
                                        "morning", "afternoon", "evening"]):
        return "Greetings! How can I be of service?"

    elif "how" in words and "you" in words:
        return "I'm doing well. All systems are operational"

    elif "status" in words:
        return "All systems are operational.\nCore status - ONLINE"

    elif "who" in words and "are" in words and "you" in words:
        return "I am Aquilon Core, a Python-based chatbot"

    else:
        return "Sorry, I am not sure how to respond to that yet"

# Opening and exit
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
