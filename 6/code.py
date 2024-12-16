#!/usr/bin/env python3

infile = "input.txt"

def get_pos_guard(map):
    for i in range(len(map)):
        if "^" in map[i]:
            return(i, map[i].index("^"), "^")
        elif "v" in map[i]:
            return(i, map[i].index("v"), "v")
        elif "<" in map[i]:
            return(i, map[i].index("<"), "<")
        elif ">" in map[i]: 
            return(i, map[i].index(">"), ">")
    return None

def get_obstruction_positions(map):
    obstructions = list()
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "#":
                obstructions.append((i, j))
    return obstructions 

def go_vertical(pos_guard, obstructions, direction):
    #print(obstructions)
    if direction == "up":
        pos_obstruction = [x for x in obstructions if x[1] == pos_guard[1] and x[0] < pos_guard[0]]
    elif direction == "down":
        pos_obstruction = [x for x in obstructions if x[1] == pos_guard[1] and x[0] > pos_guard[0]]
        
    if not pos_obstruction:
        return((None,None,None), False)
    
    diff_pos = [abs(x[0] - pos_guard[0]) for x in pos_obstruction]
    pos_new_obstruction = diff_pos.index(min(diff_pos))
    if direction == "up":
        new_pos = (pos_obstruction[pos_new_obstruction][0]+1, pos_obstruction[pos_new_obstruction][1], ">")
    elif direction == "down":
        new_pos = (pos_obstruction[pos_new_obstruction][0]-1, pos_obstruction[pos_new_obstruction][1], "<")
    return(new_pos, True)

def go_horizontal(pos_guard, obstructions, direction):
    if direction == "left":
        pos_obstruction = [x for x in obstructions if x[0] == pos_guard[0] and x[1] < pos_guard[1]]
    elif direction == "right":
        pos_obstruction = [x for x in obstructions if x[0] == pos_guard[0] and x[1] > pos_guard[1]]
        
    if not pos_obstruction:
        return((None,None,None), False)
    
    diff_pos = [abs(x[1] - pos_guard[1]) for x in pos_obstruction]
    pos_new_obstruction = diff_pos.index(min(diff_pos))
    if direction == "left":
        new_pos = (pos_obstruction[pos_new_obstruction][0], pos_obstruction[pos_new_obstruction][1]+1, "^")
    elif direction == "right":
        new_pos = (pos_obstruction[pos_new_obstruction][0], pos_obstruction[pos_new_obstruction][1]-1, "v")
    return(new_pos, True)

def get_visited_pos(new_pos_guard, pos_guard, direction, vp):
    new_visited_pos = list()
    if direction == "^":
        for x in range(int(new_pos_guard[0]), int(pos_guard[0])+1):
            if (x, pos_guard[1]) not in vp:
                new_visited_pos.append((x, pos_guard[1]))
    elif direction == "v":
        for x in range(int(pos_guard[0])+1, int(new_pos_guard[0])+1):
            if (x, pos_guard[1]) not in vp:
                new_visited_pos.append((x, pos_guard[1]))
    elif direction == "<":
        for x in range(int(new_pos_guard[1])+1, int(pos_guard[1])+1):
            if (pos_guard[0], x) not in vp:
                new_visited_pos.append((pos_guard[0], x))
    elif direction == ">":
        for x in range(int(pos_guard[1])+1, int(new_pos_guard[1])+1):
            if (pos_guard[0], x) not in vp:
                new_visited_pos.append((pos_guard[0], x))
    
    return new_visited_pos

def add_final_pos(pos_guard, vp, shape):
    if pos_guard[2] == "^":
        return(get_visited_pos((0, pos_guard[1]), pos_guard, "^", vp))
    elif pos_guard[2] == "v":
        return(get_visited_pos((shape[0]-1, pos_guard[1]), pos_guard, "v", vp))
    elif pos_guard[2] == "<":
        return(get_visited_pos((pos_guard[0], 0), pos_guard, "<", vp))
    elif pos_guard[2] == ">":
        return(get_visited_pos((pos_guard[0], shape[1]-1), pos_guard, ">", vp))

def parcours(pos_guard, obstruction_positions, visited_pos, map_shape):
    turn_pos = list()

    continue_parcours = True
    while continue_parcours:
        #print(obstruction_positions)
        if pos_guard[2] == "^":
            new_pos_guard, continue_parcours = go_vertical(pos_guard, obstruction_positions, "up")
        elif pos_guard[2] == "v":
            new_pos_guard, continue_parcours = go_vertical(pos_guard, obstruction_positions, "down")
        elif pos_guard[2] == "<":
            new_pos_guard, continue_parcours = go_horizontal(pos_guard, obstruction_positions, "left")
        elif pos_guard[2] == ">":
            new_pos_guard, continue_parcours = go_horizontal(pos_guard, obstruction_positions, "right")
        
        if new_pos_guard in turn_pos:
            return False
        
        turn_pos.append(new_pos_guard)

        if new_pos_guard[0] != None:
            visited_pos.extend(get_visited_pos(new_pos_guard, pos_guard, pos_guard[2], visited_pos))
        else:
            visited_pos.extend(add_final_pos(pos_guard, visited_pos, map_shape))

        pos_guard = new_pos_guard   
    return visited_pos

with open(infile) as f:
    map = [list(x) for x in f.read().split("\n")]

pos_guard = get_pos_guard(map)
map_shape = (len(map), len(map[0]))
visited_pos = [(int(pos_guard[0]),int(pos_guard[1]))]
obstruction_positions = get_obstruction_positions(map)

#Part 1
visited_pos_final = parcours(pos_guard, obstruction_positions, visited_pos.copy(), map_shape)
print(len(visited_pos_final))

#Part 2
nb_pos_loop = 0
count = 0
for vp in visited_pos_final:
    
    new_obstruction = obstruction_positions.copy()
    new_obstruction.append(vp)
    bla = parcours(pos_guard, new_obstruction, visited_pos.copy(), map_shape)
    if not bla:
        nb_pos_loop += 1

    print(f"{count} / {len(visited_pos_final)} / {nb_pos_loop}")
    count += 1
print(nb_pos_loop)