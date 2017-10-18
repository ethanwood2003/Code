bill = ['Bill Gates', 42, 30000,'software']
shirley = ['Shirley Bassey', 45, 40000, 'music']
stephen = ['Stephen Hawking', 65, 45000, 'science']

shirleydic = {'name':'Shirley Bassey','age':45,'salary':40000,'job':'music'}
billdic = {'name':'Bill Gates','age':42,'salary':30000,'job':'software'}
stephendic = {'name':'Stephen Hawking','age':65,'salary':45000,'job':'science'}

print("shirley[-1] = " + shirley[-1])
print("bill[0].split()[-1] = " + bill[0].split()[-1])
print("shirley[2]*1.25 = " + str(shirley[2]*1.25))

# this is a list of lists
people = [bill, shirley, stephen]

# this is a list of dictionaries
peoplelist = [billdic, shirleydic, stephendic]

film_genres = {'Star Wars' : 'Sci-fi', 'Lord of the Rings' : 'Fantasy', 'The Godfather' : 'Crime'}

print(film_genres)

print(people)

print(billdic['name'],shirleydic['salary'])
print(billdic['name'].split()[-1])
print(stephendic['salary']*1.25)

# this creates an infinite loop
while True:

	userinput = input('please enter your data search: ')

	# this loop assigns "d" (loop variable) to each member of the peoplelist list in turn.
	for d in peoplelist:
		# if the input is not a key in the current dictionary d then print the error message.
		if userinput not in d:
			print("it's not in the dictionary, knob head!")
			# break out of the loop because there is no point checking the remaining values of "d".
			break
		else:
			# this line prints the name of the person in "d" followed by the dictionary key
			# requested and then its value.
			print(d.get("name") + "'s " + userinput + " is "+ str(d.get(userinput)))
# quality program!