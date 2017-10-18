
# THe below statement uses "def" which defines a function of our own making called "isEven()"
# we can then use this isEven() later in the main body of the program.

def isEven(number):
	is_even_number = False # this initialises a boolean variable to False as we assume it's odd to start with.
	if int(number) % 2 == 0:  # this used the modulus function to check if the remainder of a divsion is 0 -- this means it is even.
		is_even_number = True # inside the if statement, we set the the boolean variable to true
	return is_even_number # finally, we get the function isEven to return this boolean value.  
	# it will return True if the number is even, and false if it is odd.



# Reads in a text file called task2.txt which contains a list of numbers in it, 
# each on a separate line (you will need to manually create task2.txt in Sublime)

with open("task2.txt", "r") as text_file: #this opens the task2.txt file and the "r" reads the file. It also assigns task2.txt to text_file
	for line in text_file: # this creates a loop over each line in the text file.
		if isEven(line): # here we use the isEven() function we defined above to check if each line the file is even.
			#if i divide num by 2 and the awns is a whole num then number is even. 
			print(line + "is even")

