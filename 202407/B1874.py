import sys
input = sys.stdin.readline

count = 1
N = int(input())
stack = []
answer = []
flag = True

for _ in range(N):
    num = int(input())
    while count <= num:
        stack.append(count)
        answer.append('+')
        count += 1
    
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        flag = False

if flag == True:
    for i in answer:
        print(i)
else:
    print("NO")