a = input('Enter three words separated by commas: ') #taking input from the user
b = a.split(',') #splitting the input at commas into words
print(sorted(b)) #using sorted function to sort the words alphabetically