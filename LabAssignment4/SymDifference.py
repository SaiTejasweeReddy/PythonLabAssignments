print('Enter two sets of numbers separated by spaces ')
#taking user input for the two required sets
a = {int(a) for a in input().split()}
b = {int(b) for b in input().split()}
#Symmetric difference
c = a ^ b
print(c)