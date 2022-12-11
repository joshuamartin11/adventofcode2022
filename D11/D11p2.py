from dataclasses import dataclass
import string
from functools import reduce
import math



with open('D11/input.txt') as f:
    lines = f.readlines()

@dataclass
class Monkey:
    items: list
    op : string
    opVal: string
    test: int
    true: int
    false: int
    handled: int = 0

monkeys = []

for i in range(0,len(lines), 7):
    startItems = []
    for word in lines[i+1].split():
        if word.strip(',').isdigit():
            startItems.append(int(word.strip(',')))
    op = lines[i+2].split()[4]
    opVal = lines[i+2].split()[5]
    for word in lines[i+3].split():
        if word.isdigit():
            test = int(word)
    for word in lines[i+4].split():
        if word.isdigit():
            true = int(word)
    for word in lines[i+5].split():
        if word.isdigit():
            false = int(word)
    newMonkey = Monkey(startItems,op,opVal,test,true,false)
    monkeys.append(newMonkey)

divs = []
for monkey in monkeys:
    divs.append(monkey.test)

lcm = reduce(lambda x, y: x * y // math.gcd(x, y), divs)



for _ in range(10000):
    for monkey in monkeys:
        while len(monkey.items) != 0:
            item = monkey.items.pop(0)
            if monkey.op == "*":
                if monkey.opVal.strip() == "old":
                    item *= item
                else:
                    item *= int(monkey.opVal)
            elif monkey.op == "+":
                if monkey.opVal.strip() == "old":
                    item += item
                else:
                    item += int(monkey.opVal)
            
            item = item % lcm

            if item % monkey.test == 0:
                monkeys[monkey.true].items.append(item)
            else:
                monkeys[monkey.false].items.append(item)

            monkey.handled += 1

handledList = []

for monkey in monkeys:
    handledList.append(monkey.handled)
handledList.sort()


print(handledList[-1] * handledList[-2])
