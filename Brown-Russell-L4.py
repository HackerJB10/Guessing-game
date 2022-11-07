'''

NAME:   Justin Brown-Russell

DATE:   9/22/22

ASSN:   LAB ASSIGNMENT L4

DESC:   THE FOLLOWING PYTHON MODULE IMPLEMENTS THE FAMOUS ROCK,
        PAPER, SCISSORS GAME.  THE RULES OF THE GAME ARE SIMPLE.
        EACH PLAYER CHOOSES A ROCK (0), PAPER(1), OR SCISSORS (2).
        THE FOLLOWING ARE WINNING PLAYS:
        
        ROCK BEATS SCISSORS
        PAPER BEATS ROCK
        SCISSORS BEATS PAPER

'''
play = input("Enter the number for what you want to play: Single play _1_  Multiple play _2_ Quit game _3_:")
turn = 0
while play != '3':
    if play == '1':
        from random import randint
        computer_choice = randint(0,2)
        user_choice = int(input("0 is Rock, 1 is paper, 2 is scissors, Enter a number:"))
        if user_choice == 0 and computer_choice == 2:
            print("Player 1 wins! PLAYER 1 CHOOSES ROCK(0) AND PLAYER 2 CHOOSES SCISSORS(2)")
            
        elif user_choice == 1 and computer_choice == 0:
            print("Player 1 wins! PLAYER 1 CHOOSES PAPER(1) AND PLAYER 2 CHOOSES ROCK(0)")
            
        elif user_choice == 2 and computer_choice == 1:
            print("Player 1 wins! PLAYER 1 CHOOSES SCISSORS(2) AND PLAYER 2 CHOOSES PAPER(1)")
            
        elif user_choice == computer_choice:
            print("Its a tie")
            
        else:
            print("Player 2 wins! Player choose " + str(computer_choice))
        play = input("Enter the number for what you want to play: Single play _1_  Multiple play _2_ Quit game _3_:")
    elif play == '2':
        multiple = int(input("How many times do you want to play?"))
    
        for i in range(multiple):
        
            from random import randint
            computer_choice = randint(0,2)
            user_choice = int(input("0 is Rock, 1 is paper, 2 is scissors, Enter a number:"))
            if user_choice == 0 and computer_choice == 2:
                print("Player 1 wins! PLAYER 1 CHOOSES ROCK(0) AND PLAYER 2 CHOOSES SCISSORS(2)")
            elif user_choice == 1 and computer_choice == 0:
                print("Player 1 wins! PLAYER 1 CHOOSES PAPER(1) AND PLAYER 2 CHOOSES ROCK(0)")
            elif user_choice == 2 and computer_choice == 1:
                print("Player 1 wins! PLAYER 1 CHOOSES SCISSORS(2) AND PLAYER 2 CHOOSES PAPER(1)")
            elif user_choice == computer_choice:
                print("Its a tie")
            else:
                print("Player 2 wins! Player choose " + str(computer_choice))
        play = input("Enter the number for what you want to play: Single play _1_  Multiple play _2_ Quit game _3_:")
print("Thank you for playing!")

   
    
    
    
    
    
    


