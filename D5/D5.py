import time
t0= time.time()

with open('D5/aoc_2022_day05_large_input.txt') as f:
    lines = f.readlines()

#Part 1
breakSpot = 0
for i, line in enumerate(lines):
    if line == "\n":
        breakSpot = i
        break

stacksInit = lines[:breakSpot-1]
movesInit = lines[breakSpot+1:]

stacks = [[] for _ in range(int(max(lines[breakSpot-1][1::4])))]
moves = [[] for _ in range(len(movesInit))]
for stack in reversed(stacksInit):
    for i, item in enumerate(stack[1::4]):
        if item.isalpha():
            stacks[i].append(item)

for i, move in enumerate(movesInit):
    for c in move.split():
        if c.isdigit():
            moves[i].append(int(c))


for move in moves:
    for i in range(move[0]):
        stacks[move[2]-1].append(stacks[move[1]-1].pop())
    
    
topChars = []
for stack in stacks:
    topChars.append(stack[-1])

t1 = time.time() - t0
print("Time elapsed: ", t1) # CPU seconds elapsed (floating point)

print(''.join(topChars))

#Part 2
stacks = [[] for _ in range(int(max(lines[breakSpot-1][1::4])))]
moves = [[] for _ in range(len(movesInit))]
for stack in reversed(stacksInit):
    for i, item in enumerate(stack[1::4]):
        if item.isalpha():
            stacks[i].append(item)

for i, move in enumerate(movesInit):
    for c in move.split():
        if c.isdigit():
            moves[i].append(int(c))


for move in moves:
    chunk = []
    for i in range(move[0]):
        chunk.append(stacks[move[1]-1].pop())
    for item in reversed(chunk):
        stacks[move[2]-1].append(item)

topChars = []
for stack in stacks:
    topChars.append(stack[-1])

t1 = time.time() - t0
print("Time elapsed: ", t1) # CPU seconds elapsed (floating point)
print(''.join(topChars))