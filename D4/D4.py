with open('D4/input.txt') as f:
    lines = f.readlines()

#Part 1
count = 0
for line in lines:
    assignments = line.split(',')
    assi1 = assignments[0].split('-')
    assi2 = assignments[1].split('-')

    if (int(assi1[0]) >= int(assi2[0]) and int(assi1[1]) <= int(assi2[1])) or (int(assi2[0]) >= int(assi1[0]) and int(assi2[1]) <= int(assi1[1])):
        print(assignments)
        count += 1
print(count)

#Part 2
count = 0
for line in lines:
    assignments = line.split(',')
    assi1 = assignments[0].split('-')
    assi2 = assignments[1].split('-')

    assi1List = [*range(int(assi1[0]),int(assi1[1])+1,1)]
    assi2List = [*range(int(assi2[0]),int(assi2[1])+1,1)]
    for num in assi1List:
        if num in assi2List:
            count += 1
            break
print(count)