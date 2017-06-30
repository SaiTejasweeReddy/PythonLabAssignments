<<<<<<< HEAD
import string   #importing the string module
alphabet = set(string.ascii_lowercase)  #creating a set of lowercased alphabet string
#welcome message
print('Checking whether a string has all letters of the alphabet')
print('If yes, the output will be TRUE')
#taking input from the user
input_string = input('Enter a string: ')
#converting all the alphabet in the input_string to lower case letters and checking if all of them a present in the alphabet set
=======
import string   #importing the string module
alphabet = set(string.ascii_lowercase)  #creating a set of lowercased alphabet string
#welcome message
print('Checking whether a string has all letters of the alphabet')
print('If yes, the output will be TRUE')
#taking input from the user
input_string = input('Enter a string: ')
#converting all the alphabet in the input_string to lower case letters and checking if all of them a present in the alphabet set
>>>>>>> 58ddbd3fcc0750ba43b43e7e948f07c1d56a48ad
print(set(input_string.lower()) >= alphabet)