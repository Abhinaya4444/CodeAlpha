import nltk
import random
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data files (for tokenization, etc.)
nltk.download('punkt')

# Define patterns and responses for chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi, how can I help you?']),
    (r'how are you?', ['I am doing well, thank you for asking!', 'I am good, how about you?']),
    (r'bye', ['Goodbye!', 'See you later!']),
    (r'(.*) your name?', ['I am a chatbot. I don\'t have a name, but you can call me Bot!']),
    (r'(.*) (help|assist|support) (.*)', ['Sure! How can I assist you today?']),
    (r'(.*) (problem|issue|error) (.*)', ['Could you describe the issue in detail? I\'ll try to help you out.']),
    (r'(.*) (love|like) (.*)', ['I am just a chatbot, I don’t have feelings, but I like helping!']),
    (r'(.*) (what|who) (.*)', ['Can you please be more specific about what you want to know?']),
    (r'(.*)', ['Sorry, I didn\'t quite get that. Can you rephrase it?'])
]

# Create chatbot object with the patterns and reflections (simple response model)
chatbot = Chat(patterns, reflections)

# Function to start the chatbot interaction
def start_chat():
    print("Hello! I'm your chatbot. Type 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Bot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"Bot: {response}")

# Run the chatbot
if __name__ == "__main__":
    start_chat()
