#Part 1
with open('D1/input.txt') as f:
    lines = f.readlines()


count = 0
counted = []
for line in lines:
    
    if(line == "\n"):
        counted.append(count)
        count = 0
    else:
        count += int(line)
    
counted.sort()

print(counted[-1])

#Part 2
print(counted[-1] + counted[-2] + counted[-3])