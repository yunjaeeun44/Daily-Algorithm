import sys
input = sys.stdin.readline
leftWord, rightWord = list(input().rstrip()), []
M = int(input())

for _ in range(M):
    command = list(input().split())
    if command[0] == 'L':
        if len(leftWord) != 0:
            tmp = leftWord.pop()
            rightWord.append(tmp)
    if command[0] == 'D':
        if len(rightWord) != 0:
            tmp = rightWord.pop()
            leftWord.append(tmp)
    if command[0] == 'B':
        if len(leftWord) != 0:
            leftWord.pop()
    if command[0] == 'P':
        leftWord.append(command[1])

print(*leftWord, *reversed(rightWord), sep='')