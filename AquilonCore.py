import string

memory = {
    "name": None,
    "facts": [],
    "last_intent": None,
    "current_intent": None
}

personality = {
    "name": "Aquilon Core",
    "style": "formal and helpful"
}
# Clean Input
def clean_input(command):
    return command.translate(
        str.maketrans("", "", string.punctuation)
    )

# Update conversation state
def update_context(intent):
    memory["last_intent"] = memory["current_intent"]
    memory["current_intent"] = intent

# Detect Intent (Dont touch future me!!!)
def detect_intent(command):
    clean_command = clean_input(command)

    words = clean_command.split()

    if clean_command == "help":
        return "help"
    elif clean_command.startswith("remember that "):
        return "remember_fact"
    elif "remember" in words or "memories" in words:
        return "retrieve_memory"
    elif clean_command == "forget everything":
        return "forget_everything"
    elif clean_command == "forget my name":
        return "forget_name"
    elif clean_command.startswith("forget that"):
        return "forget_fact"
    elif clean_command.startswith("my name is "):
        return "set_name"

    elif "name" in words and (
        "what" in words or "whats" in words
        or "tell" in words or "know" in words
    ):
        return "retrieve_name"

    elif any(word in words for word in [
        "hello", "hi", "hey", "morning", "afternoon", "evening"
    ]):
        return "greeting"
    elif "how" in words and "you" in words:
        return "how_are_you"
    elif "status" in words:
        return "status"
    elif "who" in words and "are" in words and "you" in words:
        return "identity"

    else:
        return "unknown"
# Generate Response
def respond(intent, clean_command):
    # Help
    if intent == "help":
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
    elif intent == "remember_fact":
        fact = clean_command.replace("remember that ", "", 1).strip()

        if fact:
            memory["facts"].append(fact)
            return f"I'll remember that: {fact}"
        else:
            return "What would you like me to remember?"

    elif intent == "retrieve_memory":
        if not memory["facts"]:
            return "I don't remember anything yet."
        else:
            return "I remember:\n- " + "\n- ".join(memory["facts"])

    elif intent == "forget_everything":
        memory["facts"].clear()
        memory["name"] = None
        return "All memories have been cleared."

    elif intent == "forget_name":
        if not memory["name"]:
            return "I don't have your name stored."

        memory["name"] = None
        return "I have forgotten your name."

    elif intent == "forget_fact":
        fact = clean_command.replace("forget that", "", 1).strip()

        if not fact:
            return "What would you like me to forget?"

        if fact in memory["facts"]:
            memory["facts"].remove(fact)
            return f"I have forgotten that: {fact}"
        else:
            return "I don't remember that."

    elif intent == "set_name":
        name = clean_command.replace("my name is ", "", 1).strip()

        if name:
            memory["name"] = name.title()
            return f"Nice to meet you, {memory['name']}!"
    # Answers
    elif intent == "retrieve_name":
        if not memory["name"]:
            return "I don't know your name yet"
        else:
            return f"Your name is {memory['name']}."

    elif intent == "greeting":
        if personality["style"] == "formal and helpful":
            return "Greetings! How can I be of service?"
        else:
            return "Hello! How can I help?"

    elif intent == "how_are_you":
        if personality["style"] == "formal and helpful":
            return "I'm doing well. All systems are operational"
        else:
            return "I'm doing great! Everything is running smoothly"

    elif intent == "status":
        return "All systems are operational.\nCore status - ONLINE"

    elif intent == "identity":
        return f"I am {personality['name']}, a Python-based chatbot"

    elif intent == "unknown" and memory["last_intent"] == "greeting":
        return "It seems we're continuing our conversation. How can I help?"

    else:
        return "Sorry, I am not sure how to respond to that yet"

def generate_response(command):
    clean_command = clean_input(command)
    intent = detect_intent(command)
    update_context(intent)

    return respond(intent, clean_command)

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
