#!/usr/bin/env python3

infile = "./input.txt"


def sep_val(list):
    #print(f"testing {list}")
    for i in range(1, len(list)):
        if list[i] > (list[i-1]+3):
            return False
        #print(f"{list[i]} {list[i-1]} ok ({list[i-1]}; {list[i-1]+3})")
    return True


def is_incr_decreasing(list):
    if all(i < j for i, j in zip(list, list[1:])):
        sep = sep_val(list)
        #print(sep)
        return(sep)
    elif all(i > j for i, j in zip(list, list[1:])):
        sep = sep_val(list[::-1])
        #print(sep)
        return(sep)
    return False


def is_safe(levels):
    if is_incr_decreasing(levels):
        return True
    for i in range(len(levels)):
        levelsC = levels.copy()
        del levelsC[i]
        if is_incr_decreasing(levelsC):
            return True
    return False

safe = 0         
with open(infile) as f:
    for line in f:
        levels = [int(x) for x in line.strip().split(" ")]
        
        incr_decr = is_safe(levels)
        
        if incr_decr:
            safe += 1

print(safe)