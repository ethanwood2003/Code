# Reads in a text file called task2.txt which contains a list of numbers in it, 
# each on a separate line (you will need to manually create task2.txt in Sublime)

with open("task2.txt", "r") as text_file: #this opens the task2.txt file and the "r" reads the file. It also assigns task2.txt to text_file
	for line in text_file: # this creates a loop over each line in the text file.
		if int(line) % 2 == 0: # the int turns line into a number. % gives the remainder after division 
			#if i divide num by 2 and the awns is a whole num then number is even. 
			
			print(line + "is even")



