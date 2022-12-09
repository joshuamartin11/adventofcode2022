def adjacent(hX, hY, tX, tY):
    if (hX == tX and abs(hY - tY) == 1) or \
    (hY == tY and abs(hX - tX) == 1) or \
    (abs(hX - tX) == 1 and abs(hY - tY) == 1) or \
    (hX == tX and hY == tY):
        return True

    return False

with open('D9/input.txt') as f:
    lines = f.readlines()



curXH = 0
curYH = 0
curXT = 0
curYT = 0
visited = []

for line in lines:
    splitLine = line.split()
    for i in range(int(splitLine[1])):
        if splitLine[0] == "U":
            curYH += 1
            if(not adjacent(curXH,curYH,curXT,curYT)):
                curYT += 1
                curXT = curXH
            if (curXT,curYT) not in visited:
                visited.append((curXT,curYT))
                    
        elif splitLine[0] == "D":
            curYH -= 1
            if(not adjacent(curXH,curYH,curXT,curYT)):
                curYT -= 1
                curXT = curXH
            if (curXT,curYT) not in visited:
                visited.append((curXT,curYT))

        elif splitLine[0] == "L":
            curXH -= 1
            if(not adjacent(curXH,curYH,curXT,curYT)):
                curXT -= 1
                curYT = curYH
            if (curXT,curYT) not in visited:
                visited.append((curXT,curYT))

        elif splitLine[0] == "R":
            curXH += 1
            if(not adjacent(curXH,curYH,curXT,curYT)):
                curXT += 1
                curYT = curYH
            if (curXT,curYT) not in visited:
                visited.append((curXT,curYT))

print(len(visited))

