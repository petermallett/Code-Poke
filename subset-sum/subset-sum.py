str = input()

try:
	num_inputs = int(str)
except ValueError:
	exit("First input must be the number of items to follow.")

activities = {}

if (not 1 <= num_inputs <= 50):
	exit("Number of items must be between 1 and 50")

for x in range(0, num_inputs):
	str = input()
	parts = str.strip().split(' ')
	if (len(parts) != 2):
		exit("Parse error: input lines must be in the form of '[name] [number]'. Encountered: '" + str + "'")
	else:
		try:
			calories = int(parts[1])
		except ValueError:
			exit("Second part of input line must be a numeric caloric value.")

		# remove zeros from list before starting so we don't have to check for zeros down below			
		if (calories != 0):
			activities[parts[0]] = calories

# input complete, compute sums until a solution is found
for x in range(0, 2**len(activities)):
	sum = 0
	templst = {}

	y = 0
	for name, value in activities.items():
		if 2**y & x:
			sum += value
			templst[name] = value

			if (sum == 0 and y != 0):
				print("\nsolution: \n")
				names = list(templst.keys())
				names.sort()
				for n in names:
					print(n)
				exit()
				
		y += 1

print('no solution')
