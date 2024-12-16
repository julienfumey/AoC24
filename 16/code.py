infile = 'example.txt'

with open(infile, 'r') as fhin:
    data = fhin.read().split('\n')

def search_possible_next_pos(maze, pos, shape, path, direction):
    possible_next_pos = list()

    xm1 = pos[0] - 1
    xp1 = pos[0] + 1
    ym1 = pos[1] - 1
    yp1 = pos[1] + 1

    if direction in ['W', 'N', 'E'] and xm1 >= 0 and maze[xm1][pos[1]] != '#':
        if (xm1, pos[1]) not in path:
            possible_next_pos.append((xm1, pos[1], 'N'))
    if direction in ['W', 'S', 'E'] and xp1 < shape[0] and maze[xp1][pos[1]] != '#':
        if (xp1, pos[1]) not in path:
            possible_next_pos.append((xp1, pos[1], 'S'))
    if direction in ['N', 'S', 'W'] and ym1 >= 0 and maze[pos[0]][ym1] != '#':
        if (pos[0], ym1) not in path:
            possible_next_pos.append((pos[0], ym1, 'W'))
    if direction in ['N', 'S', 'E'] and yp1 < shape[1] and maze[pos[0]][yp1] != '#':
        if ((pos[0], yp1)) not in path:
            possible_next_pos.append((pos[0], yp1, 'E'))

    return possible_next_pos

def parcours_connexe(pos, direction, maze, score, shape, possible_path, path):
    path.append(pos)
    if maze[pos[0]][pos[1]] == 'E':
        possible_path.append({'score': score, 'path': path})
    
    possible_next = search_possible_next_pos(maze, pos, shape, path, direction)
    for pn in possible_next:
        print(pn)
        pscore = 0
        if pn[2] != direction:
            pscore += 1000
            parcours_connexe((pn[0],pn[1]), pn[2], maze, score+pscore+1, shape, possible_path, path)
    
    #check

maze = [list(x) for x in data]
shape = (len(maze), len(maze[0]))

start_pos = [(i,maze[i].index('S')) for i in range(len(maze)) if 'S' in maze[i]][0]
direction = "E"
path = list((start_pos))
possible_path = list() 
print(start_pos)
possible_next = search_possible_next_pos(maze, start_pos, shape, path, direction)

for pn in possible_next:
    print(pn)
    pscore = 0
    if pn[2] != direction:
        pscore += 1000
    parcours_connexe((pn[0],pn[1]), pn[2], maze, pscore+1, shape, possible_path, path)

print(possible_path)