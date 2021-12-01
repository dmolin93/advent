code = 0
characters = 0
with open("input8.txt") as f:
    input = f.readlines()
for line in input:
    line.strip()
    code += len(line[0:-1])
    line = line[1: -2]
    characters += len(line)
    if "\\" in line:
        index = 0
        while index < len(line[:-1]):
            if line[index] == "\\":
                if line[index + 1] == "\\" or line[index + 1] == "\"":
                    characters -= 1
                    index += 1
                elif line[index + 1] == "x":
                    characters -= 3
                    index += 1
            index += 1
print code - characters
