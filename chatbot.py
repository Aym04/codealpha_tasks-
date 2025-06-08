# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 02:10:26 2025

@author: aymane
"""

# Basic Chatbot

# Function to get the chatbot's response based on user input
def chatbot_response(user_input):
    # Convert input to lowercase to make matching easier
    user_input = user_input.lower()

    # Predefined responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "what's your name" in user_input:
        return "I'm Chatbot, your friendly assistant."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that. Can you try asking something else?"

# Main loop to keep the chatbot running
print("Chatbot: Hi! I'm Chatbot. Type 'bye' to exit.")
while True:
    # Get user input
    user_input = input("You: ")
    # Get and print chatbot's response
    response = chatbot_response(user_input)
    print("Chatbot:", response)
    # Exit if the user says bye
    if "bye" in user_input.lower():
        break