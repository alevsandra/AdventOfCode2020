def find_row(seat_nr):
    max_row = 127
    min_row = 0
    for n in range(7):
        if seat_nr[n] == "F":
            max_row = max_row - int((max_row - min_row) / 2) - 1
        if seat_nr[n] == "B":
            min_row += int((max_row - min_row) / 2) + 1
    return min_row


def find_col(seat_nr):
    max_col = 7
    min_col = 0
    for m in range(-3, 0, 1):
        if seat_nr[m] == "L":
            max_col = max_col - int((max_col - min_col) / 2) - 1
        if seat_nr[m] == "R":
            min_col += int((max_col - min_col) / 2) + 1
    return min_col


x = []

filename = "input"
with open(filename) as file:
    content = file.read().splitlines()
    for row in content:
        x.append(row)

max_val = 0
plane = [[0] * 8 for j in range(128)]

for i in range(len(x)):
    new_ID = find_row(x[i]) * 8 + find_col(x[i])
    plane[find_row(x[i])][find_col(x[i])] = new_ID
    if new_ID > max_val:
        max_val = new_ID

print(max_val)
for i in range(5, 110):
    for j in range(8):
        if plane[i][j] == 0:
            print("row: " + str(i) + " column: " + str(j))
            print("ID: ", i * 8 + j)
