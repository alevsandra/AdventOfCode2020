def find_encryption_weakness(number, xmas, mn_index, mx_index):
    while sum(xmas[mn_index:mx_index]) < number:
        mx_index += 1
    if sum(xmas[mn_index:mx_index]) == number:
        print(max(xmas[mn_index:mx_index]) + min(xmas[mn_index:mx_index]))
    else:
        find_encryption_weakness(number, xmas, mn_index + 1, mn_index + 1)


filename = "input"
with open(filename) as file:
    content = file.read().splitlines()
    x = []
    i = 0
    lastAdded = 0
    for i in range(len(content)):
        if i < 25:
            x.append(int(content[i]))
        else:
            mX = sum(sorted(x, reverse=True)[:2])
            mN = sum(sorted(x, reverse=False)[:2])
            if mX < int(content[i]) or mN > int(content[i]):
                invalid_nr = int(content[i])
                print(invalid_nr)
                break
            else:
                x[lastAdded] = int(content[i])
                if lastAdded + 1 < 25:
                    lastAdded += 1
                else:
                    lastAdded = 0
    x.clear()
    for i in range(len(content)):
        x.append(int(content[i]))
find_encryption_weakness(invalid_nr, x, 0, 0)

