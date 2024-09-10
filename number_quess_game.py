from random import randint

print("\nLets play a game!!\n")

tries = 0
randNumb = randint(1,100)

while True:
    player_guess = int(input("Give a number (1-100): "))

    if player_guess == randNumb:
        print("You win!!")
        break
    elif player_guess < randNumb:
        print("Your number is to low\n")
        tries += 1
    elif player_guess > randNumb:
        print("Your number is to high\n")
        tries += 1
    else:
        print("Wrong input!")

print(f"You win in {tries} quesses!")
a = input("\n")
