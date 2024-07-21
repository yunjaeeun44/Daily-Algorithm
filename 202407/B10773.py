import sys
input = sys.stdin.readline

K = int(input())
answer = []
for _ in range(K):
    num = int(input())
    if num == 0:
        answer.pop()
    else:
        answer.append(num)
        
print(sum(answer))

