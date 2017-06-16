lenString = input('Enter the length of the Rectangle ')#taking the input 'length'
breaString = input('Enter the breadth of the Rectangle ') #taking the input 'breadth'

#converting length and breadth to integers in order to perform arithmetic operations
len = int(lenString)
brea = int(breaString)
#calculating the perimeter of rectange
peri = 2 * (len + brea)
print('Perimeter of the Rectangle is ', peri)#printing the output