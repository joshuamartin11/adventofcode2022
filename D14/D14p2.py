with open('D14/input.txt') as f:
    lines = f.readlines()

board = [["." for _ in range(400)] for _ in range(200)]
for line in lines:
    splitLine = line.split(" -> ")
    for i in range(len(splitLine)-1):
        split1 = splitLine[i].split(",")
        split2 = splitLine[i + 1].split(",")

        if split1[0].strip() == split2[0].strip():
            if int(split1[1]) < int(split2[1]):
                for j in range(int(split1[1]),int(split2[1]) + 1):
                    board[j][int(split1[0]) - 300] = "#"
            else:
                for j in range(int(split1[1]),int(split2[1]) - 1, -1):
                    board[j][int(split1[0]) - 300] = "#"
        elif split1[1].strip() == split2[1].strip():
            if int(split1[0]) < int(split2[0]):
                for j in range(int(split1[0]),int(split2[0]) + 1):
                    board[int(split1[1])][j - 300] = "#"
            else:
                for j in range(int(split1[0]),int(split2[0]) - 1,-1):
                    board[int(split1[1])][j - 300] = "#" 
maxNum = 0
for i, line in enumerate(board):
    if "#" in line:
        maxNum = i

for i in range(len(board[0])):
    board[maxNum + 2][i] = "#"



count = 0
finished = False


while board[0][200] != "o":
    
    curX = 200
    curY = -1
    while True:
        if curY + 1 >= len(board):
            finished = True
            break

        if board[curY + 1][curX] == ".":
            curY += 1
        elif board[curY + 1][curX - 1] == ".":
            curY += 1
            curX -= 1
        elif board[curY + 1][curX + 1] == ".":
            curY += 1
            curX += 1
        else:
            board[curY][curX] = "o"
            count += 1
            break
print(count)