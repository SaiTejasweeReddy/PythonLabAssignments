import random
# lists for users to enter a position
list_X = []
list_O = []
result = "" # storing the output in a string
# these are false when no one played and are used to complete each turn of both users
O_Check = False
X_Check = False
# drawing game board initially
def print_horiz_line(): # printing horizontal lines
  return " --- "
def print_vert_line(): # printing vertical lines
    return "|    "
def print_X(): # to print X
    return "| X  "
def print_O(): # to print O
    return "| O  "
# function for first user
def user1():
    global X_Check
    check = False;
    verify = False
    # asking user for position of the cell on board
    list1 = input("Enter row and column for user 1 as row,col :").split(",")
    if(len(list1[0]) == 1 and len(list1[1]) == 1):
        verify = True
    else:
        verify = False
        print("Please check your input")
        user1()

    global list_X
    # seeing if the cell is taken
    if((list1 in list_X) or (list1 in list_O)):
        check = False;
        print("That is taken. Try another spot.")
        user1()
    else:
        check = True
    # if the cell is empty, printing X
    if(check == True and verify == True):
        list_X.append(list1)
        print_user()
        X_Check = True
# function for user 2
def user2():
    global O_Check
    check = False
    verify = False
    # asking user for position of the cell on board
    list2 = input("Enter row and column for user 2 as row,col :").split(",")
    if (len(list2[0]) == 1 and len(list2[1]) == 1):
        verify = True
    else:
        verify = False
        print("Please check your input")
        user2()

    global list_O
    # seeing if the cell is taken
    if ((list2 in list_X) or (list2 in list_O)):
        check = False
        print("That is taken. Try another spot.")
        user2()
    else:
        check = True
    # if the cell is empty, printing O
    if (check == True and verify == True):
        list_O.append(list2)
        print_user()
        O_Check = True

# printing game board after each input from the users
def print_user():
    global result
    game = ""
    # looping all the rows and columns
    for i in range(0, 3):
        # horizontal line
        game = game + print_horiz_line() * 3 + "\n"
        for j in range(0, 3):
            # printing X if row,col matches
            if([str(i+1),str(j+1)] in list_X):
                game = game + print_X()
            # printing O if row,col matches
            elif ([str(i + 1), str(j + 1)] in list_O):
                game = game + print_O()
            # printing borders
            else:
                game = game + print_vert_line()
        game = game + print_vert_line()
        game = game + "\n"
    # horizontal line
    game = game + print_horiz_line() * 3
    # printing the resultant board
    result = game

def main():
    global result
    global list_X
    global list_O
    global X_Check
    global O_Check
    i = 0
    #deciding who's turn it is
    while(len(list_X)<5 or len(list_O)<4):
        if((i+1)%2 == 0):
            user2()
        else:
            user1()
        print(result)
        if(X_Check == True or O_Check == True):
            i = i + 1
            X_Check = False
            O_Check = False

    print("THE END")
main()