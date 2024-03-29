import random

def roll():
    min_value = 1 
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

value = roll()


while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            print("must be between 2-4 players: ")
            break
        else:
            print("invalid, Try Again")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

     for player_idx in range(players):
        print("\nPlayer Number" , player_idx + 1, "Turn Just Started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would You like to Roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("you just rolled a 1! Turn Done!")
                break
            else:
                current_score += value
                print("You Rolled a " , value)

            print("Your Score is", current_score)
            
        player_scores[player_idx] += current_score
        print("Your Total score is:", player_scores[player_idx])

max_score = max(player_scores)
player_winning = player_scores.index(max_score)
print("Player Number", player_winning + 1, 
      "is the winner with a score of:", max_score )


    