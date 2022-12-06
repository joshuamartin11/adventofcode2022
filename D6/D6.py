with open('D6/input.txt') as f:
    line = f.readline()
    
found = False
for i in range(len(line) - 4):
    curStringSOP = line[i: i+4]
    curStringSOM = line[i: i+14]

    #Part 1
    
    if(len(set(curStringSOP)) == len(curStringSOP) and not found):
        print(i+4)
        found = True
    #Part 2
    if(len(set(curStringSOM)) == len(curStringSOM)):
        print(i+14)
        break




