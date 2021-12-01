input = "hepxxyzz"
print input
new_password = ""

while not new_password:
    for index, c in enumerate(reversed(input)):
        new = list(reversed(input))
        if c != "z":
            c = chr(ord(c) + 1)
            new[index] = c
            input = "".join(reversed(new))
            break
        else:
            c = "a"
            new[index] = c
            input = "".join(reversed(new))
    if "i" in input or "o" in input or "l" in input:
        continue
    found = False
    first_pair = 0
    for i in range(len(input[:-1])):
        if input[i] == input[i + 1]:
            if first_pair == 0:
                first_pair = i + 1
            elif i == first_pair:
                continue
            if (input[i] + input[i + 1]) != (input[first_pair - 1] + input[first_pair]):
                found = True
                break
    if not found:
        continue
    for i in range(len(input[:-3])):
        c = input[i]
        if input[i + 1] == chr(ord(c) + 1) and input[i + 2] == chr(ord(c) + 2):
            new_password = input
            break
print new_password        
