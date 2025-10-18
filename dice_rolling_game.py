import random

counter=0
while True:
    choice=input("Roll the dice (y/n): ").lower()
    if choice=="y":
        counter+=1
        dies=int(input("Enter the number of dies: "))
        for x in range(1,dies+1):
            print(f"{random.randint(1,6)}")
    elif choice=="n":
        print(f"You have rolled the dice {counter} times")
        break
    else:
        print("Enter (Y/N)")
