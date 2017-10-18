# *all comments are for the line of code below.
# Imports random number generator. 
from random import randint

# Creates a varible to hold the lottery numbers (set to zero to start with).
winning_number=[0,0,0,0,0,0]

# "i" is a loop variable which goes from 0 to 5. This loop populates the winning number list with
# with 6 random numbers.
for i in range (0,6):
	# This line creates a random number which is assigned to "rand_num"
	rand_num = randint(1,49)
	# This checks if the random number is a duplicate. The while is used to insure that if the new
	# is itself a duplicate then it will be generated again until it's unique.
	while rand_num in winning_number:
		# This is debug code that states whether or not a duplicate number was generated.
		print("duplicate number " +  str(rand_num) + " -- generating a new one...")
		# This generates another number in the place of the duplicate. If this newly generated 
		# number is also a duplicate the while loop will catch it in the next iteration.
		rand_num = randint(1,49)
	# This line assigns the now unique random number to the "winning_number" list.
	winning_number[i] = rand_num

#This creates a variable which has the 6 winning numbers (generated in the for loop) and sorts them.
winning_number_sorted = sorted(winning_number)	

# This prints the sorted list of unique, random, numbers.
print(str(winning_number_sorted))
# pretty dank.