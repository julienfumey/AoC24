#!/usr/bin/env python3

infile = "./input.txt"

table = list()

with open(infile) as f:
    for line in f:
        table.append(line.strip())

#print(table)

nb_xmas = 0
for i in range(len(table)):
    for j in range(len(table[i])):
        if table[i][j] == "X":
            #1 search on N, NE, NW
            if i >= 3:
                if (table[i-1][j] == "M") & (table[i-2][j] == "A") & (table[i-3][j] == "S"):
                    nb_xmas += 1
                    print(f"X ({i}, {j}) N")
                
                if j >= 3:
                    if (table[i-1][j-1] == "M") & (table[i-2][j-2] == "A") & (table[i-3][j-3] == "S"):
                        nb_xmas += 1
                        print(f"X ({i}, {j}) NW")
                if j < len(table[i])-3:
                    if (table[i-1][j+1] == "M") & (table[i-2][j+2] == "A") & (table[i-3][j+3] == "S"):
                        nb_xmas += 1
                        print(f"X ({i}, {j}) NE")
            #2 search on S, SE, SW
            if i < len(table)-3:
                if (table[i+1][j] == "M") & (table[i+2][j] == "A") & (table[i+3][j] == "S"):
                    nb_xmas += 1
                    print(f"X ({i}, {j}) S")
                
                if j >= 3:
                    if (table[i+1][j-1] == "M") & (table[i+2][j-2] == "A") & (table[i+3][j-3] == "S"):
                        nb_xmas += 1
                        print(f"X ({i}, {j}) SW")
                if j < len(table[i])-3:
                    if (table[i+1][j+1] == "M") & (table[i+2][j+2] == "A") & (table[i+3][j+3] == "S"):
                        nb_xmas += 1
                        print(f"X ({i}, {j}) SE")
            
            #3 search on W
            if j >= 3:
                if (table[i][j-1] == "M") & (table[i][j-2] == "A") & (table[i][j-3] == "S"):
                    nb_xmas += 1
                    print(f"X ({i}, {j})W")
            
            #4 search on E
            if j < len(table[i])-3:
                if (table[i][j+1] == "M") & (table[i][j+2] == "A") & (table[i][j+3] == "S"):
                    nb_xmas += 1
                    print(f"X ({i}, {j}) E")
                
            #print(f"X ({i}, {j})")
print(nb_xmas)


#part 2
nb_x_mas = 0
for i in range(1,len(table)-1):
    for j in range(1,len(table[i])-1):
        if table[i][j] == "A":
            if (table[i-1][j-1] == "M") & (table[i-1][j+1] == "M") & (table[i+1][j-1] == "S") & (table[i+1][j+1] == "S"):
               nb_x_mas += 1
            
            if (table[i-1][j-1] == "S") & (table[i-1][j+1] == "S") & (table[i+1][j-1] == "M") & (table[i+1][j+1] == "M"):
                nb_x_mas += 1
            
            if (table[i-1][j-1] == "M") & (table[i-1][j+1] == "S") & (table[i+1][j-1] == "M") & (table[i+1][j+1] == "S"):
                nb_x_mas += 1
            
            if (table[i-1][j-1] == "S") & (table[i-1][j+1] == "M") & (table[i+1][j-1] == "S") & (table[i+1][j+1] == "M"):
                nb_x_mas += 1

            #if (table[i-1][j-1] == "M") & (table[i-1][j+1] == "S") & (table[i+1][j-1] == "S") & (table[i+1][j+1] == "M"):
            #    nb_x_mas += 1

            #if (table[i-1][j-1] == "S") & (table[i-1][j+1] == "M") & (table[i+1][j-1] == "M") & (table[i+1][j+1] == "S"):
            #    nb_x_mas += 1

print(nb_x_mas)


"""
M M
 A
S S

S S
 A
M M

M S
 A
M S

S M
 A
S M

M S
 A
S M

S M
 A
M S
"""