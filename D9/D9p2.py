def adjacent(hX, hY, tX, tY):
    if (hX == tX and abs(hY - tY) == 1) or \
    (hY == tY and abs(hX - tX) == 1) or \
    (abs(hX - tX) == 1 and abs(hY - tY) == 1) or \
    (hX == tX and hY == tY):
        return True

    return False

with open('D9/input.txt') as f:
    lines = f.readlines()

numKnot = 50

curXs = [0 for _ in range(numKnot)]
curYs = [0 for _ in range(numKnot)]

visited = []

for line in lines:
    splitLine = line.split()

    for _ in range(int(splitLine[1])):
        if splitLine[0] == "U":
            curYs[0] += 1
                    
        elif splitLine[0] == "D":
            curYs[0] -= 1

        elif splitLine[0] == "L":
            curXs[0] -= 1

        elif splitLine[0] == "R":
            curXs[0] += 1

        for i in range(1, numKnot):
            if(not adjacent(curXs[i-1],curYs[i-1],curXs[i],curYs[i])):
                if curXs[i] > curXs[i - 1]:
                    curXs[i] -= 1
                if curXs[i] < curXs[i - 1]:
                    curXs[i] += 1
                if curYs[i] < curYs[i - 1]:
                    curYs[i] += 1
                if curYs[i] > curYs[i - 1]:
                    curYs[i] -= 1

            if (curXs[-1],curYs[-1]) not in visited:
                visited.append((curXs[-1],curYs[-1]))
                        
print(len(visited))

