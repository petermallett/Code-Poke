set = [3, 4, 9, 14, 15, 19, 28, 37, 47, 50, 54, 56, 59, 61, 70, 73, 78, 81, 92, 95, 97, 99]

sums = [0,]

for x in set:
	temp = []
	for y in sums:
		sum = x + y
		if (sum <= set[-1]):
			temp.append(sum)
	sums.extend(temp)

count = 0
for x in sums:
	if x in set:
		count += 1

print(count - len(set))
