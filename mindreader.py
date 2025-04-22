import random

# Global score and count trackers
count_zero = 0
count_one = 0
player_score = 0
computer_score = 0

# Update how many times player entered 0 or 1
def update_counts(human_input):
    global count_zero, count_one
    if human_input == 0:
        count_zero += 1
    else:
        count_one += 1
    print("Count of 0s:", count_zero)
    print("Count of 1s:", count_one)

# Computer predicts based on player input history
def prediction():
    if count_zero > count_one:
        return 0
    elif count_one > count_zero:
        return 1
    else:
        return random.randint(0, 1)

# Score update: computer scores if it guessed right, otherwise player scores
def update_score(human_input, computer_predict):
    global computer_score, player_score
    if human_input == computer_predict:
        computer_score += 1
        print("Computer scored!")
    else:
        player_score += 1
        print("Player scored!")

    print("Player score:", player_score)
    print("Computer score:", computer_score)

# Game function where HUMAN always inputs first
def game():
    global count_zero, count_one, player_score, computer_score
    # Reset everything before starting
    count_zero = 0
    count_one = 0
    player_score = 0
    computer_score = 0

    print("🎮 Let's play! You guess first. Computer tries to predict you.")
    print("First to score 3 points wins.\n")

    while True:
        try:
            user = int(input("Enter 0 or 1: "))
            while user not in [0, 1]:
                print("Invalid input.")
                user = int(input("Enter a valid number (0 or 1): "))
        except ValueError:
            print("Please enter a number.")
            continue

        update_counts(user)
        comp_guess = prediction()
        print("Computer guessed:", comp_guess)
        update_score(user, comp_guess)

        if player_score == 3:
            print("\n You won!")
            break
        elif computer_score == 3:
            print("\n Computer won. Try again!")
            break

# Start the game
game()
