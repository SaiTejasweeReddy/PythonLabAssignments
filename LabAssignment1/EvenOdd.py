num1String = input('Please enter an integer: ')#taking a number from the user to check if it is even or odd
num1 = int(num1String)#converting a string type input to integer type in order to perform arithmetic operations on it

if (num1%2 == 0):#if the number is divisible by 0, it is printed to be EVEN
    print('The number is EVEN')
else:         #if the number is not divisible by 0, it is printed to be ODD
    print('The number is ODD')