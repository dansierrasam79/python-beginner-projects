import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

print("Guess the number (between 1 and 10):")

while True:
    # Get the user's guess
    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    # Compare the guess with the secret number
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number.")
        break
