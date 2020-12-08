import re


def find_bag(dictionary, bag_name, all_bags, shinyGoldBag, found = False):
    if found:
        print(shinyGoldBag)
    else:
        new_content = []
        for rule in all_bags:
            for i in range(len(bag_name)):
                if bag_name[i] in rule:
                    x = rule.split(" ")
                    if x[0] + ' ' + x[1] != bag_name[i] and x[0] + ' ' + x[1] not in dictionary:
                        dictionary[x[0] + ' ' + x[1]] = x[4:]
                        new_content.append(x[0] + ' ' + x[1])
        if new_content:
            find_bag(dictionary, new_content, all_bags, shinyGoldBag + len(new_content))
        else:
            find_bag(dictionary, new_content, all_bags, shinyGoldBag, True)


def how_many_bags(dictionary, all_rules, inside, found = False):
    if found:
        print(inside - 1)
    else:
        for bag in list(dictionary):
            for rule in all_rules:
                if re.match(bag, rule):
                    x = rule.split(' ')
                    for w in range(len(x)):
                        if x[w].isdigit():
                            if x[w+1] + ' ' + x[w+2] in dictionary:
                                dictionary[x[w+1] + ' ' + x[w+2]] += int(x[w])*dictionary[bag]
                            else:
                                dictionary[x[w + 1] + ' ' + x[w + 2]] = int(x[w]) * dictionary[bag]
                    inside += int(dictionary[bag])
                    dictionary.pop(bag)
                    break
        if len(dictionary) > 0:
            how_many_bags(dictionary, all_rules, inside)
        else:
            how_many_bags(dictionary, all_rules, inside, True)


filename = "input"
with open(filename) as file:
    content = file.read().splitlines()
    d = {}
    find_bag(d, ['shiny gold'], content, 0)
    d.clear()
    d['shiny gold'] = 1
    how_many_bags(d, content, 0)
