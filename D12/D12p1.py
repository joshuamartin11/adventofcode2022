def findNeighbours(n, board):
    neighbours = [(n[0]-1, n[1]), (n[0]+1, n[1]), (n[0], n[1]-1), (n[0], n[1]+1)]
    # print(len(board[0]))
    neighbours = [coord for coord in neighbours if coord[0] >= 0 and coord[1] >= 0 and coord[0] < len(board) and coord[1] < len(board[0])-1]
    # print(neighbours)
    neighbours = [coord for coord in neighbours if (ord(board[n[0]][n[1]]) - ord(board[coord[0]][coord[1]]) >= -1 and ord(board[n[0]][n[1]]) - ord(board[coord[0]][coord[1]]) < 26) or (board[n[0]][n[1]] == "z" and board[coord[0]][coord[1]] == "E") or (board[n[0]][n[1]] == "S" and board[coord[0]][coord[1]] == "a") or (board[n[0]][n[1]] == "y" and board[coord[0]][coord[1]] == "E")]

    return(neighbours)
with open('D12/input.txt') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == "S":
            start = (i,j)

# start = (20,0)

queue = []
explored = []
queue.append([start])
explored.append(start)

while len(queue) != 0:
    path = queue.pop(0)

    node = path[-1]
    if lines[node[0]][node[1]] == "E":
        print(len(path) - 1)
        # for p in path:
        #     print(lines[p[0]][p[1]])
        # print(path)
        break
    for neighbour in findNeighbours(node,lines):
        if neighbour not in explored:
            explored.append(neighbour)
            newPath = list(path)
            newPath.append(neighbour)
            queue.append(newPath)


display = [["."] * len(lines[0]) for _ in range(len(lines))]

display[path[-1][0]][path[-1][1]] = 'E'


for i, p in enumerate(path[0:-1]):
    new = list(lines[p[0]])

    if (p[0] < path[i+1][0]):
        display[p[0]][p[1]] = "v"
    elif(p[0] > path[i+1][0]):
        display[p[0]][p[1]] = "^"
    elif(p[1] < path[i+1][1]):
        display[p[0]][p[1]] = ">"
    else:
        display[p[0]][p[1]] = "<"
display[start[0]][start[1]] = 'S'
for line in display:
    print(''.join(line))
