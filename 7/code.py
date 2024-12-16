import itertools

infile = "input.txt"

with open(infile, "r") as f:
    data = [x.split(':') for x in f.read().split("\n")]

final_val = 0
for calcul in data:
    result_expected = int(calcul[0].strip())
    values = [int(x) for x in calcul[1].strip().split(' ')]

    operations = list(itertools.product(['*', '+', '||'], repeat=len(values)-1))
    
    for o in operations:
        result = values[0]
        for i in range(0, len(values)-1):
            if o[i] == '+':
                result += values[i+1]
            elif o[i] == '*':   
                result *= values[i+1]
            else:
                result = int(f"{result}{values[i+1]}")

        if result == result_expected:
            final_val += result
            break

print(final_val)