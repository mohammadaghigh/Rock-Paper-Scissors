from random import randint

#create a list of play options
p = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = p[randint(0,2)]


player = False
def ShowPlay(player,computer):
    print("You Play: " + player )
    print("Computer Play: " + computer)

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        ShowPlay(player,computer)
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            ShowPlay(player,computer)
            print("You lose!", computer, "covers", player)
        else:
            ShowPlay(player,computer)
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            ShowPlay(player,computer)
            print("You lose!", computer, "cut", player)
        else:
            ShowPlay(player,computer)
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            ShowPlay(player,computer)
            print("You lose...", computer, "smashes", player)
        else:
            ShowPlay(player,computer)
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = p[randint(0,2)]