import random #importing the 'random' module for making a random selection of numbers from 0 to 9
guessesTaken = 0 #number of guesses taken is initialized to 0 in the beginning
print('You will be given 6 chances to guess right.')#this message appears first
number = random.randint(0, 9)#selecting a random number from 0 to 9
while guessesTaken < 6: #a loop for the user to guess the number right in the given 6 chances
     print('Take a guess from 0 to 9.') #asking the user to select a number each time till the guess is right
     guess = input()
     guess = int(guess)

     guessesTaken = guessesTaken + 1 #number of guesses taken is incremented each time the loop is executed

     if guess < number:
         print('Your answer is low than required.') #this is printed if the user enters a number lesser than the randomly selected number

     if guess > number:
         print('Your answer is high than required.') #this is printed if the user enters a number greater than the randomly selected number

     if guess == number:
         break #if user guesses right, the loop is exited

if guess == number:
     print('Your answer is PERFECT!! Congratulations!') #this is printed for a correct guess

if guess != number: #this is implemented if the user is not able to guess in six chances
     number = str(number)
     print('Nope. The number was ' + number) #if the user is nt able to guess, the number is revealed