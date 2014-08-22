import random, sys

print "Welcome to Tic-Tac-Toe!\n"
print "Below shows the board layout with its corresponding values:\n"

spot = range(0,10)

def board():
    print spot[1],"|",spot[2],"|",spot[3]
    print "----------"
    print spot[4],"|",spot[5],"|",spot[6]
    print "----------"
    print spot[7],"|",spot[8],"|",spot[9]

board()

def team_select():    
    team_input = raw_input("\nPlease select a team (X or O): ").upper()
    
    if team_input == "X" or team_input == "O":
        print "Okay, you are %s's.\n" %team_input
        first_move(team_input)
    else:
        print "Sorry, this input is invalid. Try again."
        team_select()

def first_move(team_input):
    random.seed()
    rand = random.randint(0,1)
    
    print "Let's determine who makes the first move.\n" 
    first_mv_input = raw_input("Please enter either a '0' or '1': ")
    
    if first_mv_input == "0" or first_mv_input == "1":
        if int(first_mv_input) == rand:
            print "Okay, you will go first."
            play(team_input)
        elif int(first_mv_input) != rand:
            print "Okay, the computer will go first."
            comp_move(team_input)
            play(team_input)            
    else:
        print "Sorry, this input is invalid. Try again.\n"
        first_move(team_input)
        
def comp_move(team_input):
    while True: 
        random.seed()
        computer = random.randint(1,9)
       
        if spot[computer] !="X" and spot[computer] !="O":
            if team_input == "X":
                spot[computer] = "O"
            elif team_input == "O":
                spot[computer] = "X"
            break;
        elif no_more_spots():
            break;    

def play_again():
    confirm = raw_input("\nDo you wish to play again (Y or N)? ").upper()
    
    if confirm == "Y":
        spot[1:10]=range(1,10)
        team_select()
    elif confirm == "N":
        sys.exit(0)
    else:
        print "Sorry, this input is invalid. Try again."
            
def win_cond(char):
    return (spot[1] == spot[2] == spot[3] == char or
            spot[4] == spot[5] == spot[6] == char or
            spot[2] == spot[8] == spot[9] == char or
            spot[1] == spot[4] == spot[7] == char or
            spot[2] == spot[5] == spot[8] == char or
            spot[3] == spot[6] == spot[9] == char or
            spot[1] == spot[5] == spot[9] == char or
            spot[3] == spot[5] == spot[7] == char)        

def check_win():
    if (win_cond("X")):
        print "\nGame over!\nX wins!"
        play_again()
    elif (win_cond("O")):
        print "\nGame over!\nO wins!"
        play_again()
    elif no_more_spots():
        print "\nGame over!\nCats game!"
        play_again()

def no_more_spots():
    for num in range(1,10):
        if spot[num] != "X" and spot[num] != "O":
            return False
    return True         

def play_input(team_input):
    play_input = raw_input("\nPlease enter a value (1-9): ")
    play_input = int(play_input)
    if 1 <= play_input <= 9:
        if spot[play_input] !="X" and spot[play_input] !="O":
            spot[play_input] = team_input
            comp_move(team_input)
        else:
            print "Sorry, this spot is already taken. Try again."
        board()
    else:
        print "Sorry, this input is invalid. Try again."
        
def play(team_input):
    while True:
        if check_win():
            break;
        elif no_more_spots():
            check_win()
            break;
        else:
            play_input(team_input)
                                    
team_select()
