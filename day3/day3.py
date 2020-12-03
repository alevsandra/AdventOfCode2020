def find_trees(right, down, x):
    y_c = 0
    x_c = 0
    trees = 0

    while x_c + right < len(x[0]) and y_c + down < len(x):
        if x[y_c + down][x_c + right] == "#":
            trees += 1
        if x_c + 2 * right >= len(x[0]) and y_c + 2 * down < len(x):
            x_c = x_c + 2 * right - len(x[0])
            y_c += down
            if x[y_c + down][x_c] == "#":
                trees += 1
        else:
            x_c += right
        y_c += down
    return trees


filename = 'input'
with open(filename) as file:
    content = file.read().splitlines()
    i = 0
    x = [[0 for row in content[0]] for j in range(len(content))]
    for row in content:
        for j in range(len(row)):
            x[i][j] = row[j]
        i += 1

# 3 right 1 down
counter = find_trees(3, 1, x)
print(counter)

# 1 right 1 down
counter2 = find_trees(1, 1, x)
print(counter2)

# 5 right 1 down
counter3 = find_trees(5, 1, x)
print(counter3)

# 7 right 1 down
counter4 = find_trees(7, 1, x)
print(counter4)

# 1 right 2 down
counter5 = find_trees(1, 2, x)
print(counter5)
print(counter * counter2 * counter3 * counter4 * counter5)
