import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

x = []

with open(os.path.join(__location__, 'input')) as file:
    content = file.read().splitlines()
    for row in content:
        x.append(int(row))

result = 0

for i in range(len(x)):
    for j in range(len(x)):
        if x[i] + x[j] == 2020:
            result = x[i] * x[j]
            break
    if result != 0:
        break

print(result)

result = 1

for i in range(len(x)):
    for j in range(len(x)):
        for l in range(len(x)):
            if x[i] + x[j] + x[l] == 2020:
                result = x[i] * x[j] * x[l]
                break
        if result != 1:
            break
    if result != 1:
        break

print(result)