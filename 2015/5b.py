nr_of_nice = 0
with open("input5.txt") as f:
	for line in f:
		for i in range(0, len(line) - 2):
			if line[i] == line[i + 2]:
				break
		else:
			continue
				
		for i in range(0, len(line) - 1):
			if line.count(line[i] + line[i + 1]) > 1:
				nr_of_nice += 1
				break
		else:
			continue
print nr_of_nice
			
			