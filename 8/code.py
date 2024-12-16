import itertools

infile = "input.txt"

with open(infile, "r") as fhin:
    data = fhin.read().split("\n")


shape = (len(data), len(data[0].strip()))
print(shape)

antennas_positions = dict()

for i in range(len(data)):
    pos = list(data[i])
    for j in range(len(pos)):
        if data[i][j] != '.':
            frequency = str(data[i][j])
            if not frequency in antennas_positions:
                antennas_positions[frequency] = [(i,j)]
            else:
                antennas_positions[frequency].append((i,j))

print(len(antennas_positions))

antinodes_positions = set()
for freq in antennas_positions:
    positions = antennas_positions[freq]
    print(positions)

    if len(positions) > 1:    
        for i1 in range(len(positions)-1):
            c1 = positions[i1]
            for i2 in range(i1+1, len(positions)):
                c2 = positions[i2] 

                pos_diff_x = c2[0] - c1[0]
                pos_diff_y = c2[1] - c1[1]

                x0 = c1[0] - pos_diff_x
                y0 = c1[1] - pos_diff_y
                
                x1 = c2[0] + pos_diff_x
                y1 = c2[1] + pos_diff_y
                      
                #print(f"==antennes: {c1}, {c2}==")
                if 0 <= x0 < shape[0] and 0 <= y0 < shape[1]:
                    pos0 = (x0,y0)
                    antinodes_positions.add(pos0)
                    #print(pos0)
            
                if 0 <= x1 < shape[0] and 0 <= y1 < shape[1]:
                    pos1 = (x1,y1)
                    antinodes_positions.add(pos1)
                    #print(pos1)
            
                
print(len(antinodes_positions))
#print(antinodes_positions)