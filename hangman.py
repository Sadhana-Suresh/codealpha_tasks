import random

def choose_word():
    words = ["python", "programming", "hangman", "developer", "challenge", "keyboard"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
    word_to_guess = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = 6
    
    print("Welcome to Hangman! Try to guess the word letter by letter.")
    
    while incorrect_guesses < max_attempts:
        print("\nWord:", display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        guessed_letters.add(guess)
        
        if guess not in word_to_guess:
            incorrect_guesses += 1
            print(f"Incorrect guess! You have {max_attempts - incorrect_guesses} attempts left.")
        else:
            print("Good job! You found a letter.")
        
        if all(letter in guessed_letters for letter in word_to_guess):
            print("\nCongratulations! You guessed the word:", word_to_guess)
            return
    
    print("\nGame Over! The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
