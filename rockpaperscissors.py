import random
guess = ["Rock", "Paper", "Scissors"]

computer = guess[random.randint(0,2)]

points_player = 0
points_computer = 0

player = False

while player == False:
    
    player = input("Rock, Paper or Scissors? ")

    if player == computer:
        print("Tie!!")
        print(f" You = {points_player} : Computer = {points_computer}")
        if points_player < 3:
            player = False

    elif player == "Rock":
        if computer == "Scissors":
            print(f"You won this round! {player} cuts {computer}.")
            points_player += 1
            print(f" You : {points_player} | Computer : {points_computer}")


            if points_player == 3:
                print("You won the Match! Congratulations!")                
                points_player = 0
                points_computer = 0
                again = input("Do you want to play another round? Yes or No? ")
                if again.lower() == "yes":
                    player = False
                else:
                    player = True

            elif points_computer == 3:
                print("You lost the Match :( Don't give up, you'll win the next one!!")                
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
            print(f"You lost this round! {computer} defeats {player}.")
            points_computer += 1
            print(f" You : {points_player} | Computer : {points_computer}")


            if points_player == 3:
                print("You won the Match! Congratulations!")                
                points_player = 0
                points_computer = 0
                again = input("Do you want to play another round? Yes or No? ")
                if again.lower() == "yes":
                    player = False
                else:
                    player = True

            elif points_computer == 3:
                print("You lost the Match :( Don't give up, you'll win the next one!!")                
                points_player = 0
                points_computer = 0
                again = input("Do you want to play another round? Yes or No? ")
                if again.lower() == "yes":
                    player = False
                else:
                    player = True
            else:
                player = False


    elif player == "Paper":
        if computer == "Rock":
            print(f"You won this round! {player} defeats {computer}.")
            points_player += 1
            print(f" You : {points_player} | Computer : {points_computer}")


            if points_player == 3:
                print("You won the Match! Congratulations!")                
                points_player = 0
                points_computer = 0
                again = input("Do you want to play another round? Yes or No? ")
                if again.lower() == "yes":
                    player = False
                else:
                    player = True

            elif points_computer == 3:
                print("You lost the Match :( Don't give up, you'll win the next one!!")                
                points_player = 0
                points_computer = 0
                again = input("Do you want to play another round? Yes or No? ")
                if again.lower() == "yes":
                    player = False
                else:
                    player = True
            else:
                player = False

        elif computer == "Scissors":
            print(f"You lost this round! {computer} cuts {player}.")

            points_computer += 1
            print(f" You : {points_player} | Computer : {points_computer}")


            if points_player == 3:
                print("You won the Match! Congratulations!")                
                points_player = 0
                points_computer = 0
                again = input("Do you want to play another round? Yes or No? ")
                if again.lower() == "yes":
                    player = False
                else:
                    player = True

            elif points_computer == 3:
                print("You lost the Match :( Don't give up, you'll win the next one!!")                
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
            print(f"You lost this round! {computer} defeats {player}.")

            points_computer += 1
            print(f" You : {points_player} | Computer : {points_computer}")


            if points_player == 3:
                print("You won the Match! Congratulations!")                
                points_player = 0
                points_computer = 0
                again = input("Do you want to play another round? Yes or No? ")
                if again.lower() == "yes":
                    player = False
                else:
                    player = True

            elif points_computer == 3:
                print("You lost the Match :( Don't give up, you'll win the next one!!")                
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
            print(f"You won this round! {player} cuts {computer}")

            points_player += 1
            print(f" You : {points_player} | Computer : {points_computer}")


            if points_player == 3:
                print("You won the Match! Congratulations!")                
                points_player = 0
                points_computer = 0
                again = input("Do you want to play another round? Yes or No? ")
                if again.lower() == "yes":
                    player = False
                else:
                    player = True

            elif points_computer == 3:
                print("You lost the Match :( Don't give up, you'll win the next one!!")                
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
        print("You need to type the words in Capital at the first Letter :). Try Again")
        player = False
       
