#!/usr/bin/env python3
import re

infile = "./input.txt"

def somme_mul(my_list):
    somme = 0
    for line in my_list:
        matches = re.findall("mul\\(([0-9]{0,3}),([0-9]{0,3})\\)", line)
        somme += sum([int(x[0])*int(x[1]) for x in matches])
    
    return somme

lines = list()
with open(infile, "r") as f:
    lines = f.readlines()

#part 1
print(somme_mul(lines))

#part 2
text = ''.join(lines)
somme2 = 0
#for line in lines:
matches = re.findall("mul\(([0-9]{0,3}),([0-9]{0,3})\)|(do\(\))|(don't\(\))", text)
go = True
for m in matches:
    print(m)
    
    if m[3] == "don't()":
        go = False
        continue
    
    if m[2] == "do()":
        go = True
        continue

    if go and m[2] == "" and m[3] == "":
        somme2 += int(m[0])*int(m[1])
    
    

#for m in matches:
#    somme2 += somme_mul(m)

print(somme2)