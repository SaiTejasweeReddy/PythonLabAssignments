print('Tic Tac Toe for 2 players') #welcome greeting
#GAME BOARD
def print_horiz_line(): #defining a function for horizontal lines
    print(" ---" * 3)
def print_vert_line(): #defining a function for vertical lines
    print("|   " * (3 + 1))
#loop for horizontal and vertical lines in consecutive lines
for index in range(3):
    print_horiz_line()    #calling the functions
    print_vert_line()
print_horiz_line() #printing the last line

print('Player 1 marks X and Player 2 marks O')

p1=input('Player 1, what is your move?(specify in row,column format)') #taking the input from the user for desired position
a,b=p1.split(",") #using split function to separate the input into row and column

