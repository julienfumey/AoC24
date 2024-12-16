from collections import defaultdict

infile = "input.txt"


with open(infile, "r") as f:
    data = f.read().split("\n")

shape = (len(data), len(data[0].strip()))
print(shape)
positions = defaultdict(list)
for i in range(len(data)):
    for j in range(len(data[i])):
        positions[int(data[i][j])].append((i,j))

def parcours_connexe(pos, positions, val, shape, pos_9):
    score = 0
    positions_to_visit = list()
    
    if pos[0] > 0 and (pos[0]-1, pos[1]) in positions[val+1]:
        positions_to_visit.append((pos[0]-1, pos[1]))
    if pos[0] < shape[0] and (pos[0]+1, pos[1]) in positions[val+1]:
        positions_to_visit.append((pos[0]+1, pos[1]))
    if pos[1] > 0 and (pos[0], pos[1]-1) in positions[val+1]:
        positions_to_visit.append((pos[0], pos[1]-1))
    if pos[0] < shape[1] and (pos[0], pos[1]+1) in positions[val+1]:
        positions_to_visit.append((pos[0], pos[1]+1))
    
    for p in positions_to_visit:
        if val+1 == 9:
            pos_9.add(p)
            score += 1
        else:
            score += parcours_connexe(p, positions, val+1, shape, pos_9)
    
    return score

trailhead_score = 0
tscore = 0
for pos in positions[0]:
    pos_9 = set()
    score = parcours_connexe(pos, positions, 0, shape, pos_9)
    tscore += score
    #print(score)
    trailhead_score += len(pos_9)

print(trailhead_score)
print(tscore)
