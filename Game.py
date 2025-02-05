import random

def choose_word():
    # List of words to choose from
    word_list = ["python", "programming", "hangman", "challenge", "developer", "algorithm", "debugging"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    # Show the word with guessed letters revealed and others as underscores
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    print("Welcome to Hangman!")

    word_to_guess = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("\nThe word has", len(word_to_guess), "letters:")
    print(display_word(word_to_guess, guessed_letters))

    while incorrect_guesses < max_incorrect_guesses:
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print("Good job! That letter is in the word.")
        else:
            incorrect_guesses += 1
            print("Wrong guess! You have", max_incorrect_guesses - incorrect_guesses, "guesses left.")

        print("\n", display_word(word_to_guess, guessed_letters))

        if all(letter in guessed_letters for letter in word_to_guess):
            print("\nCongratulations! You guessed the word:", word_to_guess)
            break
    else:
        print("\nGame over! The word was:", word_to_guess)

# Run the game
if __name__ == "__main__":
    hangman()


# import random

# # List of words for the game
# words = ["python", "java", "hangman", "code", "debug"]

# # Randomly select a word
# word = random.choice(words)
# guessed_word = ["_"] * len(word)  # Create a list of underscores for the word
# attempts = 6  # Number of incorrect guesses allowed

# print("Welcome to Hangman!")
# print("Word to guess: ", " ".join(guessed_word))

# while attempts > 0:
#     guess = input("Guess a letter: ").lower()

#     # Check if the guess is valid
#     if len(guess) != 1 or not guess.isalpha():
#         print("Please enter a single letter.")
#         continue

#     # Check if the letter is in the word
#     if guess in word:
#         print(f"Good job! '{guess}' is in the word.")
#         # Reveal the guessed letter in the word
#         for i, letter in enumerate(word):
#             if letter == guess:
#                 guessed_word[i] = guess
#     else:
#         attempts -= 1
#         print(f"Wrong guess! You have {attempts} attempts left.")

#     # Display the current state of the word
#     print("Word to guess: ", " ".join(guessed_word))

#     # Check if the player has guessed the entire word
#     if "_" not in guessed_word:
#         print(f"Congratulations! You guessed the word: {word}")
#         break
# else:
#     print(f"Game over! The word was: {word}")
