import re

anyoneYes = 0
everyoneYes = 0

filename = "input"
with open(filename) as file:
    x = []
    content = file.read().splitlines()
    for row in content:
        for letter in row:
            if re.match('[a-z]', letter) and (letter not in x):
                anyoneYes += 1
                x.append(letter)
        if row == "":
            x.clear()
    # part 2
    d = {}
    everyone = 0
    for row in content:
        for letter in row:
            if letter in d:
                amount = d[letter]
                d[letter] = amount+1
            elif everyone == 0:
                d[letter] = 1
        if row != "":
            everyone += 1
        if row == "" or row == content[-1]:
            for letter in d:
                if d[letter] == everyone:
                    everyoneYes += 1
            d.clear()
            everyone = 0

print(anyoneYes)
print(everyoneYes)


