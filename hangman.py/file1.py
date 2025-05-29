import random

WORDS = {
    "easy": [("apple", "A fruit"), ("cat", "A small animal"), ("book", "Used for reading")],
    "medium": [("python", "A programming language"), ("guitar", "A musical instrument"), ("planet", "A celestial body")],
    "hard": [("algorithm", "Used in programming"), ("microscope", "Used in labs"), ("philosophy", "Study of knowledge")]
}

MAX_ATTEMPTS = {
    "easy": 8,
    "medium": 6,
    "hard": 5
}

def get_word(difficulty):
    return random.choice(WORDS[difficulty])

def display_word(word, guessed):
    return ' '.join([letter if letter in guessed else '_' for letter in word])

def hangman():
    print("🎮 Welcome to Hangman!")
    
    # Difficulty selection
    while True:
        difficulty = input("Choose difficulty (easy / medium / hard): ").lower()
        if difficulty in WORDS:
            break
        print("❌ Invalid choice. Please select from easy, medium, or hard.")

    word, hint = get_word(difficulty)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = MAX_ATTEMPTS[difficulty]

    print(f"\n💡 Hint: {hint}")
    print(f"You have {max_wrong} ❤ lives. Let's begin!")
    print(display_word(word, guessed_letters))

    while wrong_guesses < max_wrong:
        guess = input("\nEnter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Enter a single alphabet.")
            continue

        if guess in guessed_letters:
            print("⚠ You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Good guess!")
        else:
            wrong_guesses += 1
            print(f"❌ Wrong! {max_wrong - wrong_guesses} ❤ lives left.")

        print(display_word(word, guessed_letters))

        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You guessed the word.")
            break
    else:
        print(f"\n💀 Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()