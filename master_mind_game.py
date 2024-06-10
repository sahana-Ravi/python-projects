"""Two players play the game against each other; let’s assume Player 1 and Player 2.

Player 1 plays first by setting a multi-digit number.
Player 2 now tries his first attempt at guessing the number.
If Player 2 succeeds in his first attempt (despite odds which are highly unlikely) he wins the game and is crowned Mastermind! If not, then Player 1 hints by revealing which digits or numbers Player 2 got correct.
The game continues till Player 2 eventually is able to guess the number entirely.
Now, Player 2 gets to set the number and Player 1 plays the part of guessing the number.
If Player 1 is able to guess the number within a lesser number of tries than Player 2 took, then Player 1 wins the game and is crowned Mastermind.
If not, then Player 2 wins the game.
The real game, however, has proved aesthetics since the numbers are represented by color-coded buttons."""

def play(name):
    num = (input("Player 1 enter your Number!: "))
    l = len(num)
    turn = 1
    while (True):
        guess = input("Player 2 Enter your guess!: ")
        x = 0
        for i in range(l):
            if num[i] == guess[i]:
                print(guess[i], end=" ")
                x = x+1
            else:
                print("X ", end=" ")
        if (x < 0):
            print("You are disqualified")
            exit(0)
        elif (turn == 1 and x == l):
            print(name +" is a MasterMind!!")
            exit(0)
        elif (x == l):
            print("Truns taken by Player1 is ", turn)
            return turn
        else:
            turn += 1

game = True
while (game):
    print("Enter names of Player 1 and Player 2: ")
    player_1, player_2 = input().split(" ")
    print("Welcome "+player_1 + " and " + player_2 + " !")
    turn_1=play(player_1)
    turn_2=play(player_2)
    if (turn_2 > turn_1):
        print(player_1+"is MasterMind!")
    elif (turn_1 > turn_2):
        print(player_2+"is MasterMind")
    else:
        print("It's a tie")
    
    
    





    

    
