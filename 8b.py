code = 0
characters = 0
with open("input8.txt") as f:
    input = f.readlines()
    for line in input:
        line.strip()
            code += len(line[0:-1])
                line = line[0: -1]
                    characters += len(line) + 4
                        if "\\" in line:
                                index = 0
                                        while index < len(line[:-1]):
                                                    if line[index] == "\\":
                                                                    if line[index + 1] == "\\" or line[index + 1] == "\"":
                                                                                        characters += 2
                                                                                                            index += 1
                                                                                                                            elif line[index + 1] == "x":
                                                                                                                                                characters += 1
                                                                                                                                                                    index += 1
                                                                                                                                                                                index += 1
                                                                                                                                                                                print characters - code

