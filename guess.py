import random

print("Welcome to the Guess My Number Game!")

while True:
    secret_number = random.randint(1, 100)
    guess_count = 0
    guess = -1

    while guess != secret_number:
        guess = int(input("Guess the secret number?" ))
        guess_count += 1

        if guess < secret_number:
            print("Too low! try again.")
        elif guess > secret_number:
            print("Too high! try again.")
        else:
            print("You guessed it!")

    print(f"It took you {guess_count} guesses.")

    # Ask if the user wants to play again
    play_again = input("Would you like to play again (yes/no)? ").strip().lower()
    if play_again != 'yes':
        print("Thank you for playing. Goodbye!")
        break
