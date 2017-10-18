# first, set the variable to 0 outside the loop.u
current_running_total = 0

for x in range(1,101):
	# inside the loop, first print x (which will go from 1 to 100)
	print("Current number = " + str(x))
	# now, increase the running total from what it was previsouly, by x.
	
	current_running_total = current_running_total + x
	# the NEW value       =. the old value plus
	print("Current running total = " + str(current_running_total))