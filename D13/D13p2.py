import ast
import copy

with open('D13/input.txt') as f:
    lines = f.readlines()

def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):

        if left < right:
            return 1
        elif left > right:
            return 0
        else:
            return 2
    if isinstance(left,list) and isinstance(right, int):

        right = [right]
        ret = compare(left,right)
        if ret != 2:
            return ret

    if isinstance(left,int) and isinstance(right, list):

        left = [left]
        ret = compare(left,right)
        if ret != 2:
            return ret

    if isinstance(left,list) and isinstance(right, list):
        while len(left) > 0 and len(right) > 0:
            leftVal = left.pop(0)
            rightVal = right.pop(0)


            
            ret = compare(leftVal,rightVal)
            if ret != 2:
                return ret

        if len(right) == 0 and len(left) != 0:
            return 0
        elif len(left) == 0 and len(right) != 0:
            return 1
        else:
            return 2


correct = 0
lists = [[[2]],[[6]]]
for i in range(0,len(lines), 3):
    lists.append(ast.literal_eval(lines[i]))
    lists.append(ast.literal_eval(lines[i+1]))

print(lists)
for i in range(len(lists)):
    for j in range(0,len(lists)-i-1):

        if compare(copy.deepcopy(lists[j]),copy.deepcopy(lists[j+1])) == 0:
            lists[j],lists[j+1] = lists[j+1], lists[j]

print((lists.index([[2]])+1) * (lists.index([[6]]) + 1))
    # if compare(list1,list2):
    #     correct += (i//3) + 1
    #     print("Correct")

    # print()

# print(correct)


