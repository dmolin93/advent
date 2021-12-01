text = "1113122113 "
print text
for i in range(50):
    new_text = ""
    count = 1
    for x in range(len(text)-1):
        if text[x] == text[x+1]:
            count += 1
        else:
            new_text += str(count) + text[x]
            count = 1
    print i
    text = new_text + " "
print len(text)-1