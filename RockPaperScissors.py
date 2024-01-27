import random

def play():
    game_tuple = ("r", "p", "s")
    player_selection = input("Select either rock (r), paper (p) or scissors (s)")
    computer_selection = random.choice(game_tuple)
    if player_selection == computer_selection:
        print("It's a tie.")
    elif winner(player_selection,computer_selection):
        print("You have won!")
    else:
        print("You have lost!")

def winner(player, computer):
    if (player == "r" and computer == "s") or (player == "s" and computer == "p") or (player == "p" and computer == "r"):
        return True
    else:
        return False

if __name__ == "__main__":
    play()
