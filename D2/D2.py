
#Part 1
with open('D2/input.txt') as f:
    lines = f.readlines()
score = 0
for line in lines:
    splitLine = line.split()
    if splitLine[0] == "A": #rock
        if splitLine[1].strip() == "X": #rock
            score += 4
        elif splitLine[1].strip() == "Y": #paper
            score += 8
        elif splitLine[1].strip() == "Z": #scissors
            score += 3
    elif splitLine[0] == "B": #paper
        if splitLine[1].strip() == "X": #rock
            score += 1
        elif splitLine[1].strip() == "Y": #paper
            score += 5
        elif splitLine[1].strip() == "Z": #scissors
            score += 9
    elif splitLine[0] == "C": #scissors
        if splitLine[1].strip() == "X": #rock
            score += 7
        elif splitLine[1].strip() == "Y": #paper
            score += 2
        elif splitLine[1].strip() == "Z": #scissors
            score += 6

print(score)

rock = 1
paper = 2
scissors = 3
#Part 2
score = 0
for line in lines:
    splitLine = line.split()
    if splitLine[0] == "A": #rock
        if splitLine[1].strip() == "X": #lose
            score += scissors
        elif splitLine[1].strip() == "Y": #draw
            score += (rock + 3)
        elif splitLine[1].strip() == "Z": #win
            score += (paper + 6)
    elif splitLine[0] == "B": #paper
        if splitLine[1].strip() == "X": #lose
            score += rock
        elif splitLine[1].strip() == "Y": #draw
            score += (paper + 3)
        elif splitLine[1].strip() == "Z": #win
            score += (scissors + 6)
    elif splitLine[0] == "C": #scissors
        if splitLine[1].strip() == "X": #lose
            score += paper
        elif splitLine[1].strip() == "Y": #draw
            score += (scissors + 3)
        elif splitLine[1].strip() == "Z": #win
            score += (rock + 6)

print(score)
