# Word Guessing Game with creativity:
# - --Randomly selects secret word from a list.
# - --Limits number of guesses to 10.
# - --Reveals secret word if not guessed within limit.
#    --Word Guessing Game -- lets go!

import random

words = ["mosiah", "moroni", "temple", "zion", "lehi"]
secret_word = random.choice(words)
guess_count = 0
max_guesses = 10
guess = ""

print("Welcome to the word guessing game!")
print(f"You have {max_guesses} attempts to guess the secret word.")

while guess != secret_word and guess_count < max_guesses:
    guess = input("What is your guess? ").lower()
    
    # Check guess length
    if len(guess) != len(secret_word):
        print(f"Your guess must be {len(secret_word)} letters long.")
        continue
    
    guess_count += 1
    
    if guess == secret_word:
        print("Congratulations! You guessed it!")
        print(f"It took you {guess_count} guesses.")
        break
    
    # Build hint string
    hint = ""
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint += guess[i].upper() + " "
        elif guess[i] in secret_word:
            hint += guess[i].lower() + " "
        else:
            hint += "_ "
    
    print(hint.strip())
    print("Your guess was not correct.")
    print(f"Guesses left: {max_guesses - guess_count}")

if guess != secret_word:
    print(f"Sorry, you ran out of guesses. The secret word was '{secret_word}'.")
