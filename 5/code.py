#!/usr/bin/env python3

import math

# open file and separate rules and messages
infile = "input.txt"


def get_indices(messages, rules):
    indices = list()
    for i in messages:
        indices.append(rules.index(i))
    return indices

def check_order(indices):
    if all(x < y for x, y in zip(indices, indices[1:])):
        return True
    return False

def get_all_subrules(i, rules):
    sublist = [x for x in rules if x[0] == i]
    return sublist
#
with open(infile) as f:
    data = f.read().split("\n")

posVide = data.index('')

rules = [x.split('|') for x in data[:posVide]]
updates = [x.split(',') for x in data[posVide+1:]]

rule_dict = dict()


def check_update(rule_dict, update):
    for i in range(len(update)):
        if not set(update[i+1:]).issubset(rule_dict[update[i]]):
            return False
    return True

def correct_update(rule_dict, update):
    for i in range(len(update)):
        while not set(update[i+1:]).issubset(rule_dict[update[i]]):
            update.append(update.pop(i))
    
    return int(update[len(update) // 2])

for rule in rules:
    if rule[0] in rule_dict:
        rule_dict[rule[0]].append(rule[1])
    else:
        rule_dict[rule[0]] = [rule[1]]

somme_part1 = 0
somme_part2 = 0
for update in updates:
    if check_update(rule_dict, update):
        somme_part1 += int(update[len(update) // 2])
    else:
        somme_part2 += correct_update(rule_dict, update)

print(somme_part1)
print(somme_part2)


"""



nb_rule_by_first = dict()
first_rule_list = sorted(set([x[0] for x in rules]))

for rule in first_rule_list:
    nb_rule_by_first[rule] = len([x for x in rules if x[0] == rule])

print(nb_rule_by_first)
print(len(first_rule_list))
# sort rules

sorted_rules = list()

#print(sorted_rules)



subrule = first_rule_list.pop(0)
sublist = [x for x in rules if x[0] == subrule]
#print(sublist)
sorted_rules.extend(sublist[0])

done_pos = [subrule]

while len(first_rule_list) > 0:
    i = first_rule_list.pop(0)
    sublist = sorted(get_all_subrules(i, rules), key=lambda x: x[1])

    min_pos = None
    for j in sublist:
        if j[1] in sorted_rules:
            if min_pos == None:
                min_pos = sorted_rules.index(j[1])
            else:
                min_pos = min(min_pos, sorted_rules.index(j[1]))
    
    if min_pos == None:
        print(i)
        sorted_rules.append(i)
        #first_rule_list.append(i)
        #continue
    else:
        sorted_rules.insert(min_pos, i)
    done_pos.append(i)
    

#print(sorted_rules)


print(sorted_rules)

#print(messages)
safe = list()
# Check which message are safe
for m in messages:
    #print(m)
    indices = get_indices(m, sorted_rules)
    #print(m)
    #print(indices)
    
    if check_order(get_indices(m, sorted_rules)):
        safe.append(m)
        #print("safe")

#print(safe)

# Get middle values
middle_value = list()
for s in safe:
    middle_value.append(s[math.floor(len(s)/2)])

sum_middle = sum([int(x) for x in middle_value])
print(sum_middle)
"""