#!/usr/bin/env python3
infile = "./input.txt"

left_list = list()
right_list = list()

with open(infile) as f:
    for line in f:
        left, right = line.split("   ")
        left_list.append(int(left))
        right_list.append(int(right))

left_list.sort()
right_list.sort()


# PART 1
somme = 0
for i in range(len(left_list)):
    somme += abs(int(right_list[i]) - int(left_list[i]))

print(f"somme of difference : {somme}")


# PART 2
similarity = 0

for i in left_list:
    similarity += int(i) * right_list.count(i)

print(f"final similarity : {similarity}")