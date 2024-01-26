import random

def clueprovider(n2g):
    print("Your clue:")
    if n2g <= 500:
        print("The number is less than or equal to 500.")
    else:
        print("The number is greater than 500.")

def guessnumber(n2g):
    guessed = 0
    points = 100
    tries = 0
    clueprovider(n2g)
    while guessed != n2g:
        guessed = int(input("Guess the randomly generated number: "))
        if guessed > n2g:
            print("Your guess", guessed, "is higher in value. Try again.")
            points -= 10
            tries += 1
        elif guessed < n2g:
            print("Your guess", guessed, "is lower in value. Try again.")
            points -= 10
            tries += 1
        else:
            print("Your guess is absolutely right. The number is", str(n2g))
            print("Congrats! You finished the game with ", str(points), "and ", str(tries), "tries")
            break;

#Main
if __name__ == "__main__":
    number2guess = random.randint(1,1000)
    print(number2guess)
    print("Welcome to the guessing game. You have to guess the number within a range of 1-1000")
    guessnumber(number2guess)