import random #Imported a mod
comp_wins = 0 #Set scoreboard
user_wins = 0

def Choose_option():  #defined a function/run a block of code when called.
    user_choice = input('pick between rock, paper, or snip:')
    if user_choice in ["Rock",'rock','r','R']:
        user_choice = 'r'
    elif user_choice in ["paper","Paper","p","P"]:
        user_choice ="p"
    elif user_choice in ["Snip","snip","S","s"]:
        user_choice = "s"
    else:
        print("pick the right option jackass")
        Choose_option()
    return user_choice
def Computer_option():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    elif comp_choice == 3:
        comp_choice = "s"
    return comp_choice
while True:
    print("")
    user_choice = Choose_option()
    comp_choice = Computer_option()
    print('')

    if user_choice == 'r':
        if comp_choice == 'r':
            print("It is a tie")
        elif comp_choice == 'p':
            print("you picked rock. The computer chose paper. You lose.')")
            comp_wins += 1
        elif comp_choice == "s":
            print('you chose rock. The computer chose snip. you win.')
            user_wins += 1
    elif user_choice == 'p':
        if comp_choice == 'r':
            print("You chose paper. The computer chose rock. You win.")
            user_wins += 1
        elif comp_choice == 'p':
            print('You chose paper. The computer chose paper. you tied.')
        elif comp_choice == "s":
            print("you chose paper. the computer picked snip. you lose")
            comp_wins += 1
    elif user_choice == "s":
            if comp_choice == "r":
                print("you picked snip. The computer picked rock. You lose")
                comp_wins += 1
            elif comp_choice == 's':
                print('You picked snip. Computer picked snip. It is a tie')
            elif comp_choice == 'p':
                print('You picked snip. Computer picked paper. You win.')
                user_wins += 1
    print('')
    print('Player wins:' + str(user_wins))
    print("computer wins: " + str(comp_wins))
    print("")
    user_choice = input("Do you want to play again? (y/n)")
    if user_choice in ["Y","y","yes","Yes"]:
        pass
    elif user_choice in ["N","n",'no','No']:
        break
    else:
        break

