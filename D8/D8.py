from dataclasses import dataclass

with open('D8/input.txt') as f:
    lines = f.readlines()

@dataclass
class Tree:
    height: int
    visible: bool = False
grid = []
for line in lines:
    gridline = []
    for c in line:
        if c.isdigit():
            tree = Tree(height=int(c))
            gridline.append(tree)
    grid.append(gridline)

visCount = 0
for line in grid:
    curMaxHeight = -1
    for tree in line:
        if tree.height > curMaxHeight and tree.visible == False:
            # print(tree.height)
            tree.visible = True
            visCount += 1 
        
        if tree.height > curMaxHeight:
            curMaxHeight = tree.height
        if tree.height == 9:
            break
    curMaxHeight = -1
    for tree in reversed(line):
        if tree.height > curMaxHeight and tree.visible == False:

            tree.visible = True
            visCount += 1
        if tree.height > curMaxHeight:
            curMaxHeight = tree.height
        if tree.height == 9:
            break  

for i in range(len(grid[0])):
    curMaxHeight = -1
    for j in range(len(grid)):
        if grid[j][i].height > curMaxHeight and grid[j][i].visible == False:
            # print(grid[j][i].height)
            
            grid[j][i].visible = True
            visCount += 1
        if grid[j][i].height > curMaxHeight:
            curMaxHeight = grid[j][i].height
        if grid[j][i].height == 9:
            break     
    curMaxHeight = -1
    for j in reversed(range(len(grid))):
        if grid[j][i].height > curMaxHeight and grid[j][i].visible == False:
            grid[j][i].visible = True
            visCount += 1
        if grid[j][i].height > curMaxHeight:
            curMaxHeight = grid[j][i].height
        if grid[j][i].height == 9:
            break
print(visCount)

maxVal = 0

for i in range(1,len(grid)-1):
    for j in range(1,len(grid[0])-1):
        score = 1
        scoreSum = 0
        for k in range(j + 1, len(grid[0])):
            scoreSum += 1
            if grid[i][k].height >= grid[i][j].height:
                break
            
        score *= scoreSum

        scoreSum = 0
        for k in reversed(range(0, j)):
            scoreSum += 1
            
            if grid[i][k].height >= grid[i][j].height:
                break
        score *= scoreSum
        scoreSum = 0
        for k in range(i + 1, len(grid)):
            scoreSum += 1
            
            if grid[k][j].height >= grid[i][j].height:
                break
        score *= scoreSum
        scoreSum = 0
        for k in reversed(range(0, i)):
            scoreSum += 1
            
            if grid[k][j].height >= grid[i][j].height:
                break
        score *= scoreSum
        
        if score > maxVal:
            maxVal = score 
    
print(maxVal)