infile = "input.txt"

with open(infile, "r") as fhin:
    data = fhin.read().split("\n")

balls = data[0].strip().split(' ')

#print(balls)
for blink in range(75):
    new_balls = list()
    for i in range(len(balls)):
        if int(balls[i]) == 0:
            new_balls.append('1')
        elif len(balls[i]) % 2 == 0:
            #print(balls[i])
            half = int(len(balls[i])/2)
            new_balls.append(str(int(balls[i][0:half])))
            new_balls.append(str(int(balls[i][half:])))
        else:
            new_balls.append(str(int(balls[i])*2024))
    balls = new_balls.copy()

print(len(balls))