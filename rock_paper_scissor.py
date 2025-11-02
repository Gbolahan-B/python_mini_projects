import random

option=["r","p","s"]
options={'r':'🪨','p':'📃','s':'✂️'}

wins=0
loose=0
played=0

while True:
    player1_win=0
    player2_win=0

    
    print("Enter mode. Enter q to quit")
    print("1.vs Computer")
    print("2.vs Human")
    choice=input(">>").lower()

    if choice=="q":
        print("\n👋 Goodbye!")
        print(f"Total matches played: {played}")
        print(f"Matches won: {wins}")
        print(f"Matches lost: {loose}")
        break
        

    while player1_win < 3 and player2_win < 3:
        
        if choice=="1":
            computer=random.choice(option)
            player1=input("Enter you choice: ").lower()

            if player1 in option:
                print(f"You choose {options[player1]}")
                print(f"Computer choose {options[computer]}")
                player2=computer
            else:
                print("Enter a valid input")
        elif choice=="2":
            player1=input("Player 1 (r/p/s): ").lower()
            player2=input("Player 2 (r/p/s): ").lower()

            if player1 not in option or player2 not in option:
                print("Enter a valid option")
                continue

        else:
            print("Invalid choice")
            break

        if (
            (player1 == "r" and player2 == "s") or
            (player1 == "s" and player2 == "p") or
            (player1 == "p" and player2 == "r")
        ):
            print("Player 1 WINS")
            player1_win+=1
        elif player2==player1:
            print("Its a TIE")
        else:
            print("Player 2 WINS")
            player2_win+=1
    played+=1
    
    if player2>player1:
        print("Player 1 won this round")
        wins+=1
    elif player1==player2:
        print("Tie round")
    else:
        print("Player 2 won this round")
        loose+=1