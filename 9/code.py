infile = "input.txt"

with open(infile, "r") as f:
    data = f.read().split("\n")

diskmap = list(data[0].strip())
#print(diskmap)

blocks = list()
for i in range(len(diskmap)):
    if i % 2 == 0:
        blocks.extend([(int(int(i/2)))]*int(diskmap[i]))
    else:
        blocks.extend(['.']*int(diskmap[i]))

blocks_part2 = blocks.copy()

#pos = 0
#while not all('.' == x for x in blocks[pos:]):
#    if blocks[pos] == '.':
#        last_val = next((x for i, x in enumerate(blocks[:pos:-1]) if x!='.'), None)
#        index = max([i for i, x in enumerate(blocks) if x == last_val])
#
#        blocks[pos], blocks[index] = blocks[index], blocks[pos]
#
#    pos += 1

#part1_sum = 0

#for i in range(0, blocks.index('.')):
#    part1_sum += int(i)*int(blocks[i])

#print(part1_sum)


# part2
max_val = max([int(x) for x in blocks_part2 if x != '.'])
print(max_val)
#print(max(list_of_val))


for val in range(max_val, 0, -1):
    pos = 0
    #last_val = next((x for i, x in enumerate(blocks_part2[:pos:-1]) if x!='.'), None)
    index = [i for i, x in enumerate(blocks_part2) if x == val]
    positions = list(filter(lambda i: len(set(blocks_part2[i:i+len(index)]))==1 and list(set(blocks_part2[i:i+len(index)]))[0] == '.', range(len(blocks_part2)-len(index))))
    
    if len(positions) > 0:
        position = min(positions)
        if position > index[0]:
            continue 

        for i in range(len(index)):
            blocks_part2[position+i] = blocks_part2[index[i]]
            blocks_part2[index[i]] = '.'

part2_sum = 0
for i in range(len(blocks_part2)):
    if blocks_part2[i] != '.':
        part2_sum += int(i)*int(blocks_part2[i])

print(part2_sum)
