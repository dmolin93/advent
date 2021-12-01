vowels = ['a', 'e', 'i', 'o', 'u']
dirty_words = ['ab', 'cd', 'pq', 'xy']
nice_strings = 0

with open("input5.txt") as f:
	for line in f:
		line = line.strip()
		nr_of_vowels = 0
		for char in line:
			for vowel in vowels:
				if char == vowel:
					nr_of_vowels += 1
					break
		if nr_of_vowels < 3:
			continue
			
		douplicate = False
		for index, char in enumerate(line[:-1]):
			if char == line[index + 1]:
				douplicate = True
				break
		if douplicate == False:
			continue
		
		found = False
		for word in dirty_words:
			if word in line:
				found = True
				break
		if found == True:
			continue
		
		nice_strings += 1
print nice_strings
