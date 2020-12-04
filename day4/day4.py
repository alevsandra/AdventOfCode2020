import string


def check_byr(byr):
    return 1920 <= byr <= 2002


def check_iyr(iyr):
    return 2010 <= iyr <= 2020


def check_eyr(eyr):
    return 2020 <= eyr <= 2030


def check_hgt(hgt):
    if hgt[len(hgt) - 2:] == "cm":
        if 150 <= int(hgt.split("cm")[0]) <= 193:
            return True
    elif hgt[len(hgt) - 2:] == "in":
        if 59 <= int(hgt.split("in")[0]) <= 76:
            return True


def check_hcl(hcl):
    if hcl[0] == "#":
        for letter in hcl[1:]:
            if letter not in string.hexdigits:
                return False
        return True


def check_ecl(ecl):
    if ecl == "amb":
        return True
    if ecl == "blu":
        return True
    if ecl == "brn":
        return True
    if ecl == "gry":
        return True
    if ecl == "grn":
        return True
    if ecl == "hzl":
        return True
    if ecl == "oth":
        return True
    return False


def check_pid(pid):
    if len(pid) == 9:
        return True


def check_record(record):
    t = []
    for m in range(len(record)):
        t = record[m].split(":")
        if t[0] == "byr":
            if not check_byr(int(t[1])):
                return False
        elif t[0] == "iyr":
            if not check_iyr(int(t[1])):
                return False
        elif t[0] == "eyr":
            if not check_eyr(int(t[1])):
                return False
        elif t[0] == "hgt":
            if not check_hgt(t[1]):
                return False
        elif t[0] == "hcl":
            if not check_hcl(t[1]):
                return False
        elif t[0] == "ecl":
            if not check_ecl(t[1]):
                return False
        elif t[0] == "pid":
            if not check_pid(t[1]):
                return False
    return True


d = {}

filename = 'input'
with open(filename) as file:
    content = file.read().splitlines()
    y = []
    i = 0
    for row in content:
        if row == '':
            i += 1
        else:
            y = row.split(' ')
            d.setdefault(i, []).extend(y)

counter = 0

for i in range(len(d)):
    if len(d[i]) == 8:
        counter += 1
    elif len(d[i]) == 7:
        cidExists = 0
        for j in range(len(d[i])):
            y = str(d[i][j]).partition(":")
            if y[0] == "cid":
                cidExists += 1
        if cidExists == 0:
            counter += 1


print(counter)

counter = 0

for i in range(len(d)):
    if len(d[i]) == 8:
        if check_record(d[i]):
            counter += 1
    elif len(d[i]) == 7:
        cidExists = 0
        for j in range(len(d[i])):
            y = str(d[i][j]).partition(":")
            if y[0] == "cid":
                cidExists += 1
        if cidExists == 0 and check_record(d[i]):
            counter += 1


print(counter)
