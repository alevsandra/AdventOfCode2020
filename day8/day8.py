def terminate_correctly(been_there, instructions):
    done_that = {}
    n = 0
    changed = 0
    accumulator = 0
    while n not in done_that and n != len(instructions):
        done_that[n] = instructions[n]
        x = instructions[n].split(' ')
        if changed == 0 and "jmp" in x[0] and n not in been_there:
            been_there[n] = instructions[n]
            n += 1
            changed = 1
        elif changed == 0 and "nop" in x[0] and n not in been_there:
            been_there[n] = instructions[n]
            n += int(x[1])
            changed = 1
        else:
            if "jmp" in x[0]:
                n += int(x[1])
            elif "acc" in x[0]:
                accumulator += int(x[1])
                n += 1
            else:
                n += 1

    if n != len(instructions):
        terminate_correctly(been_there, instructions)
    else:
        print(accumulator)


filename = "input"
with open(filename) as file:
    content = file.read().splitlines()
    acc_val = 0
    d = {}
    i = 0
    while i not in d:
        d[i] = content[i]
        x = content[i].split(' ')
        if "jmp" in x[0]:
            i += int(x[1])
        elif "acc" in x[0]:
            acc_val += int(x[1])
            i += 1
        else:
            i += 1
print(acc_val)
# part 2
terminate_correctly({}, content)
