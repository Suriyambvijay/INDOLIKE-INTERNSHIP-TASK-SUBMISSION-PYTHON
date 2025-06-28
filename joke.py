import random

def get_random_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the computer go to the doctor? Because it had a virus!",
        "Parallel lines have so much in common... it’s a shame they’ll never meet.",
        "Why do Java developers wear glasses? Because they don't C#!",
        "What do you call i8 hobbits? A hob-byte!",
        "I told my computer I needed a break, and now it won't stop sending me vacation ads.",
        "Why was the math book sad? Because it had too many problems.",
        "Debugging: Being the detective in a crime movie where you are also the murderer.",
        "How do you comfort a JavaScript bug? You console it.",
        "Why was the cell phone wearing glasses? Because it lost its contacts!"
    ]
    
    return random.choice(jokes)

# --- Main Execution ---
if __name__ == "__main__":
    print("Welcome you all to the Random Joke Generator!")
    while True:
        input("\nPress Enter to hear a joke... (or Ctrl+C to quit)\n")
        print(">>", get_random_joke())
