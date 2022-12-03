with open('D3/input.txt') as f:
    lines = f.readlines()

#Part 1
count = 0

for line in lines:
    string1, string2 = line[:len(line)//2], line[len(line)//2:]

    for c in string1:
        if c in string2:
            if c.islower():
                count += (ord(c) - 96)
            else:
                count += (ord(c) - 38)
            break
print(count)

#Part 2
count = 0

for i in range(0,len(lines),3):
    for c in lines[i]:
        if c in lines[i+1] and c in lines[i+2]:
            if c.islower():
                count += (ord(c) - 96)
            else:
                count += (ord(c) - 38)
            break

print(count)
