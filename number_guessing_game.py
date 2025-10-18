import random

def play_game():
    low,high=1,100

    played=0
    all_attempts=[]
    is_playing=True
    while is_playing:
        status=input("Play (y/n)").lower()
        attempt=0
        num=random.randint(low,high)
        if status=="y":
            played+=1
            for x in range(5):
                guess=int(input("Guess the number between 1 and 100: "))
                attempt+=1
                if guess<num:
                    print("Too low")
                elif guess>num:
                    print("Too high")
                else:
                    print(f"Congratulations. You got it in {attempt} attempts")
                    all_attempts.append(attempt)
                    break
            else:
                print("You have used your attempt")
                print(f"The number was {num}")
        elif status=="n":
            is_playing=False
            if not all_attempts:
                print("Good bye")
            else:
                print(f"You played {played} times")
                print(f"You best score is {min(all_attempts)} attempts")

if __name__=="__main__":
    play_game()