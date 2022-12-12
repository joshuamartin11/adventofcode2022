def findNeighbours(n, board):
    neighbours = [(n[0]-1, n[1]), (n[0]+1, n[1]), (n[0], n[1]-1), (n[0], n[1]+1)]
    # print(len(board[0]))
    neighbours = [coord for coord in neighbours if coord[0] >= 0 and coord[1] >= 0 and coord[0] < len(board) and coord[1] < len(board[0])-1]
    # print(neighbours)
    neighbours = [coord for coord in neighbours if ord(board[n[0]][n[1]]) - ord(board[coord[0]][coord[1]]) >= -1 or (board[n[0]][n[1]] == "z" and board[coord[0]][coord[1]] == "E") or (board[n[0]][n[1]] == "S" and board[coord[0]][coord[1]] == "a")]

    return(neighbours)
with open('D12/input.txt') as f:
    lines = f.readlines()

starts = []

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == "S" or c == "a":
            starts.append((i,j))

# start = (20,0)

lengths = []

for start in starts:

    queue = []
    explored = []
    queue.append([start])
    explored.append(start)

    while len(queue) != 0:
        path = queue.pop(0)

        node = path[-1]
        if lines[node[0]][node[1]] == "E":
            lengths.append(len(path)-1)
            break
        for neighbour in findNeighbours(node,lines):
            if neighbour not in explored:
                explored.append(neighbour)
                newPath = list(path)
                newPath.append(neighbour)
                queue.append(newPath)

print(min(lengths))

# for p in path:
#     new = list(lines[p[0]])

#     new[p[1]] = "#"

#     lines[p[0]] = ''.join(new)

# for line in lines:
#     print(line.strip())
