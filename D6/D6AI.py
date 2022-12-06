#Optimised by AI
with open('D6/input.txt') as f:
    line = f.readline()
    
found = False
if len(line) >= 14:
    for i in range(len(line) - 14):
        curStringSOP = line[i: i+4]
        curStringSOM = line[i: i+14]

        # Part 1

        if not found and all(ch not in curStringSOP[:j] for j, ch in enumerate(curStringSOP)):
            print(i+4)
            found = True

        # Part 2
        if all(ch not in curStringSOM[:j] for j, ch in enumerate(curStringSOM)):
            print(i+14)