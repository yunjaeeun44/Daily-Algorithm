inputStr = input()

strList = []
tmp = '+'
for i in inputStr:
    if i == '-' or i == '+':
        strList.append(tmp)
        tmp = ''
    tmp += i
strList.append(tmp)

intList = [0]
for i in strList:
    if i[0] == '-':
        intList.append(int(i))
    else:
        tmp = intList.pop()
        if tmp < 0:
            intList.append(tmp - int(i))
        else:
            intList.append(tmp + int(i))

print(sum(intList))