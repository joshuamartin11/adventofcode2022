with open('D7/input.txt') as f:
    lines = f.readlines()

dirs = {}
curDir = []

id = 0

for line in lines:
    
    splitLine = line.split()
    if(splitLine[0] == "$"):
        if splitLine[1] == "cd":
            if splitLine[2].strip() == "..":
                curDir.pop()
            else:
                # if splitLine[2].strip() not in dirs:
                dirs[id] = 0
                curDir.append(id)
                id += 1
    elif splitLine[0].isdigit():
        for dir in curDir:
            dirs[dir] += int(splitLine[0])


sum = 0
for val in list(dirs.values()):
    if val <= 100000:
        sum += val

print(sum)

#Part 2

unused = 70000000 - dirs[0]
values = list(dirs.values())
values.sort() 


for val in values:
    if(val + (70000000 - dirs[0]) >= 30000000):
        print(val)
        break
