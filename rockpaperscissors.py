import random
guess = ["Rock", "Paper", "Scissors"]

computer = guess[random.randint(0,2)]

points_player = 0
points_computer = 0

player = False

while player == False:
    
    player = input("\nRock, Paper or Scissors? ")

    if player == computer:
        print("\n\nTie!!")
        print(f"\nYou = {points_player} : Computer = {points_computer}\n")
        if points_player < 3:
            player = False

    elif player == "Rock":
        if computer == "Scissors":
            print(f"\n\nYou won this round! {player} cuts {computer}.")
            points_player += 1
            print(f"\nYou : {points_player} | Computer : {points_computer}\n")


            if points_player == 3:
                print("You won the Match! Congratulations!\n\n")                
                points_player = 0
                points_computer = 0
                again = input("\nDo you want to play another round? Yes or No? ")
                if again.lower() == "yes":
                    player = False
                else:
                    player = True

            elif points_computer == 3:
                print("You lost the Match :( Don't give up, you'll win the next one!!\n\n")                
                points_player = 0
                points_computer = 0
                again = input("\nDo you want to play another round? Yes or No? ")
                if again.lower() == "yes":
                    player = False
                else:
                    player = True
            else:
                player = False


        elif computer == "Paper":
            print(f"\n\nYou lost this round! {computer} defeats {player}.")
            points_computer += 1
            print(f"\nYou : {points_player} | Computer : {points_computer}\n")


            if points_player == 3:
                print("You won the Match! Congratulations!\n\n")                
                points_player = 0
                points_computer = 0
                again = input("\nDo you want to play another round? Yes or No? ")
                if again.lower() == "yes":
                    player = False
                else:
                    player = True

            elif points_computer == 3:
                print("You lost the Match :( Don't give up, you'll win the next one!!\n\n")                
                points_player = 0
                points_computer = 0
                again = input("\nDo you want to play another round? Yes or No? ")
                if again.lower() == "yes":
                    player = False
                else:
                    player = True
            else:
                player = False


    elif player == "Paper":
        if computer == "Rock":
            print(f"\n\nYou won this round! {player} defeats {computer}.")
            points_player += 1
            print(f"\nYou : {points_player} | Computer : {points_computer}\n")


            if points_player == 3:
                print("You won the Match! Congratulations!\n\n")                
                points_player = 0
                points_computer = 0
                again = input("\nDo you want to play another round? Yes or No? ")
                if again.lower() == "yes":
                    player = False
                else:
                    player = True

            elif points_computer == 3:
                print("You lost the Match :( Don't give up, you'll win the next one!!\n\n")                
                points_player = 0
                points_computer = 0
                again = input("\nDo you want to play another round? Yes or No? ")
                if again.lower() == "yes":
                    player = False
                else:
                    player = True
            else:
                player = False

        elif computer == "Scissors":
            print(f"\n\nYou lost this round! {computer} cuts {player}.")

            points_computer += 1
            print(f"\nYou : {points_player} | Computer : {points_computer}\n")


            if points_player == 3:
                print("You won the Match! Congratulations!\n\n")                
                points_player = 0
                points_computer = 0
                again = input("Do you want to play another round? Yes or No? ")
                if again.lower() == "yes":
                    player = False
                else:
                    player = True

            elif points_computer == 3:
                print("You lost the Match :( Don't give up, you'll win the next one!!\n\n")                
                points_player = 0
                points_computer = 0
                again = input("Do you want to play another round? Yes or No? ")
                if again.lower() == "yes":
                    player = False
                else:
                    player = True
            else:
                player = False

    elif player == "Scissors":
        if computer == "Rock":
            print(f"\n\nYou lost this round! {computer} defeats {player}.")

            points_computer += 1
            print(f"\nYou : {points_player} | Computer : {points_computer}\n")


            if points_player == 3:
                print("You won the Match! Congratulations!\n\n")                
                points_player = 0
                points_computer = 0
                again = input("Do you want to play another round? Yes or No? ")
                if again.lower() == "yes":
                    player = False
                else:
                    player = True

            elif points_computer == 3:
                print("You lost the Match :( Don't give up, you'll win the next one!!\n\n")                
                points_player = 0
                points_computer = 0
                again = input("Do you want to play another round? Yes or No? ")
                if again.lower() == "yes":
                    player = False
                else:
                    player = True
            else:
                player = False

        elif computer == "Paper":
            print(f"\n\nYou won this round! {player} cuts {computer}")

            points_player += 1
            print(f"\nYou : {points_player} | Computer : {points_computer}\n")


            if points_player == 3:
                print("You won the Match! Congratulations!\n\n")                
                points_player = 0
                points_computer = 0
                again = input("Do you want to play another round? Yes or No? ")
                if again.lower() == "yes":
                    player = False
                else:
                    player = True

            elif points_computer == 3:
                print("You lost the Match :( Don't give up, you'll win the next one!!\n\n")                
                points_player = 0
                points_computer = 0
                again = input("Do you want to play another round? Yes or No? ")
                if again.lower() == "yes":
                    player = False
                else:
                    player = True
            else:
                player = False

    else:
        print("\nOnly write 'Rock', 'Paper' or 'Scissors'. Try Again :)")
        player = False
       
