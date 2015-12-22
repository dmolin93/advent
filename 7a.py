values = {}
index = 0
with open("input7.txt") as f:
    data = f.readlines()
while not values.has_key("a"):
    for line in data:
        index += 1
        left, right = line.split("->")
        left = left.strip()
        right = right.strip()
        if not values.has_key(right):
            expressions = left.split(" ")
            if len(expressions) == 1:
                try:
                    values[right] = int(expressions[0])
                    continue
                except ValueError:
                    if values.has_key(expressions[0]):
                        values[right] = values[expressions[0]]
                    continue
            elif len(expressions) == 2:
                try:
                    values[right] = ~ int(expressions[1])
                    continue
                except ValueError:
                    if values.has_key(expressions[1]):
                        values[right] = ~ values[expressions[1]]
                    continue
            else:
                valueOne = 0
                valueTwo = 0
                operator = expressions[1]
                try:
                    valueOne = int(expressions[0])
                except ValueError:
                    if values.has_key(expressions[0]):
                        valueOne = values[expressions[0]]
                    else:
                        continue
                try:
                    valueTwo = int(expressions[2])
                except ValueError:
                    if values.has_key(expressions[2]):
                        valueTwo = values[expressions[2]]
                    else:
                        continue
                if operator == "AND":
                    values[right] = valueOne & valueTwo
                elif operator == "OR":
                    values[right] = valueOne | valueTwo
                elif operator == "RSHIFT":
                    values[right] = valueOne >> valueTwo
                elif operator == "LSHIFT":
                    values[right] = valueOne << valueTwo
print index
print values["a"]