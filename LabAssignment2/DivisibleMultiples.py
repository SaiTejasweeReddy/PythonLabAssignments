#welcome text
print('This program prints all the numbers divisible by 7 and multiples of 5 within a given range')
#taking input from the user for the desired range of numbers
lower=int(input("Enter the lower range:"))
upper=int(input("Enter the upper range:"))
#writing a nested loop wherein each element in the given range is checked for its divisibility with 7 and multiplicity with 5
for i in range (lower,upper+1):
    if(i%7==0 and i%5==0):
        print(i)    #printing the result in each loop