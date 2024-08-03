N = int(input())
L = list(map(int, input().split()))

L.sort()
tmp = 0
answer = 0

for i in L:
    tmp += i
    answer += tmp

print(answer)