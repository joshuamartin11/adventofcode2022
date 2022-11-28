with open('D0\input.txt') as f:
    lines = f.readlines()

calculated = []

for line in lines:
    calculated.append((int(line)//3) - 2)

print(sum(calculated))
