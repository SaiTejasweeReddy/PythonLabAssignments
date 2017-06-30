aList=[] #initializing an empty list
#a loop for taking tuples as input from the user
for index in range(0,3): #taking three tuples here but number of tuples can also be increased
    a=str(input('Enter a tuple: '))
    b=tuple(map(int,a.split(','))) #converting the input from the user to tuples
    aList.append(b) #appending the tuples to the list
print('The created list of tuples is: ')
print(aList) #the final list
c= sorted(aList, key=lambda x: x[-1]) #sorting the list based on the ascending order of the second elements of the tuples
print('Sorted list: ')
print(c) #required sorted list
