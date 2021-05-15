#importing random function to work with
import random

#-----global variables-----
#the game is defined here
game=["Rock","Paper","Scissor"]

#variables to store the winner count
computer_count=0
player_count=0
tie_count=0
match_count=0

#to check if player wants to play further or not
valid=True
play_again_choice="0"

#variable to store computer's choice
computer_choice="0"

#variable to store player's choice
player_choice="0"

#playing the game
#game is being played
def play():
    global computer_choice

    #storing computer's choice in a variable
    computer_choice=random_choice()

    #calling player input to take input from player everytime the game is played
    player_input()

    #calling check_winner to check for a winner
    check_winner()

    return

#check if there is a winner
def check_winner():
    #to make changes to the global variables
    global computer_count
    global player_count
    global tie_count
    global match_count
        #checking winning condition for computer
    if computer_choice=="Rock" and player_choice=="Scissor" or computer_choice=="Paper" and player_choice=="Rock" or computer_choice=="Scissor" and player_choice=="Paper":
        computer_count+=1
        match_count+=1
        print(f"Computer's choice: {computer_choice}.\nPlayer's choice: {player_choice}.\nThe winner is Computer. Player lost.")

    #checking winning condition for the player
    elif player_choice=="Rock" and computer_choice=="Scissor" or player_choice=="Paper" and computer_choice=="Rock" or player_choice=="Scissor" and computer_choice=="Paper":
        player_count+=1
        match_count+=1
        print(f"Player's choice: {player_choice}.\nComputer's choice: {computer_choice}.\nThe winner is Player. Computer lost.")
    else:
        tie_count+=1
        match_count+=1
        print(f"Player's choice: {player_choice}.\nComputer's choice: {computer_choice}.\nThis game is a tie.")
        

#choosing randomly from stone, paper or scissor
def random_choice():
    computer_choice=random.choice(game)
    return computer_choice

#defining funtion to take input from player
def player_input():
    global player_choice

    #player's choice is being taken as an input to proceed with the game
    player_choice=input("Enter r for rock, p for paper or s for scissor to begin the game.\n")

    #converting to lower case
    player_choice=player_choice.lower()

    #checking if player has entered a valid choice
    while player_choice not in ["r","p","s"]:
        player_choice=input("Invalid input. Please try again.\nEnter r for rock, p for paper or s for scissor to continue with the game\n")

    #assigning player with the corresponding value of his choice
    if player_choice=="r":
        player_choice=game[0]
    elif player_choice=="p":
        player_choice=game[1]
    elif player_choice=="s":
        player_choice=game[2]
    return

#to check if player wants to play the game again or not
def play_again():
    global valid
    play_again_choice=input("Do you want to play again? Y/N\n")
    play_again_choice=play_again_choice.upper()
    while play_again_choice not in ["Y","N","n","y"]:
        play_again_choice=input("Invalid input. Please try again.\n")
    if play_again_choice=="Y" or play_again_choice=="y":
        valid=True
    else:
        valid=False
    return

#playing the game
while valid is True:
    play()
    play_again()
print(f"A total of {match_count} matches have been played.")
print(f"Computer won {computer_count} matches.")
print(f"Player won {player_count} matches.")
print(f"{tie_count} matches were tie.")
if computer_count>player_count:
    print(f"Computer won with {computer_count} matches.")
elif player_count>computer_count:
    print(f"Player won with {player_count} matches.")