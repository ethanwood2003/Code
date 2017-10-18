# step 1 : generate a random number between 1 and 10.
from random import randint
the_answer = randint(1,10)
guessed_correctly = False
amtgus = 1
while guessed_correctly == False:
	guess = int(input("Guess a number between 1 and 10."))
	if the_answer == guess:
		print("Well Done!")
		guessed_correctly = True
		print("you guessed it in " + str(amtgus) +" guess(es)")
	elif guess < the_answer:
		print("Too low try again.")
		amtgus = amtgus+1
	else:
		print("Too high try again.")
		amtgus = amtgus+1