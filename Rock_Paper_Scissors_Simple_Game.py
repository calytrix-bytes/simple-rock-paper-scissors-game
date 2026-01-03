import random
replay_input = "yes"
while replay_input == "yes":
    print("Welcome to Rock-Paper-Scissors!")
    print("Rules: First to score 3 points wins the match.")
    print("Type your choice: rock, paper, or scissors.")
    player_score = 0
    computer_score = 0 
    while computer_score < 3 and player_score < 3:
        player_choice = input("Enter your move (rock/paper/scissors): ").lower()
        while player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid move. Try again.")
            player_choice = input("Enter your move (rock/paper/scissors): ").lower()
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print("You chose", player_choice.capitalize(), "| The computer chose", computer_choice.capitalize())
        if player_choice == computer_choice:
            print("It's a tie! Destiny refuses to pick a side.")
        elif ((player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "scissors" and computer_choice == "paper") or
        (player_choice == "paper" and computer_choice == "rock")):
            print("You win this round! Wanna quit while you're ahead?...just saying")
            player_score+=1
        else:
            print("You lose this round! Maybe it's time to unplug the computer?")
            computer_score+=1
        print("Score: You - ", player_score, "| Computer - ", computer_score)
    if player_score == 3:
        print("YOU WIN! The computer has entered its sad mode.")
    if computer_score == 3:
        print("Computer wins the match! Better luck next time!")
    replay_input = input("Do you wish to play again? (Yes/No)").lower()
    while replay_input not in ["yes", "no"]:
        replay_input = input("I didn't get that. Please type 'yes' or 'no': ").lower()
print("Thanks for playing! See you next time.")
