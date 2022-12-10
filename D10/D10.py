

import textwrap


with open('D10/testinput.txt') as f:
    lines = f.readlines()
cycle = 0
curX = 1

checks = [20,60,100,140,180,220]

crt = []

sum = 0

for line in lines:
    splitLine = line.split()
    incVal = 0
    if splitLine[0] == "addx":
        incVal = int(splitLine[1])
        wait = 2
    elif splitLine[0] == "noop":
        wait = 1
    waitCur = 0

    while waitCur < wait:
        cycle += 1
        waitCur += 1

        #######################Part 2######################
        if curX >= (cycle % 40 ) - 2 and curX <= (cycle%40):
            crt.append("#")
        else:
            crt.append(".")
        ####################################################


        if cycle in checks:
            sum += (curX * cycle)
    


    if incVal != 0:
        curX += incVal
    
print(sum)



for line in textwrap.wrap(''.join(crt), 40):
    print(line)
# print(''.join(crt))



    