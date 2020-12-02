
filename = 'input'
with open(filename) as file:
    content = file.read().splitlines()
    i = 0
    y = []
    x = [[0] * 4 for j in range(len(content))]
    for row in content:
        y = row.split(" ")
        x[i][0] = y[0].partition('-')[0]
        x[i][1] = y[0].partition('-')[2]
        x[i][2] = y[1].partition(':')[0]
        x[i][3] = y[2]
        i += 1

counter = 0

for j in range(len(x)):
    word = x[j][3]
    lilCounter = 0
    for m in range(len(word)):
        if x[j][2] == word[m]:
            lilCounter += 1
    if int(x[j][0]) <= lilCounter <= int(x[j][1]):
        counter += 1

print(counter)

counter = 0

for j in range(len(x)):
    word = x[j][3]
    lilCounter = 0
    if x[j][2] == word[int(x[j][0]) - 1]:
        lilCounter += 1
    if x[j][2] == word[int(x[j][1]) - 1]:
        lilCounter += 1
    if lilCounter == 1:
        counter += 1

print(counter)