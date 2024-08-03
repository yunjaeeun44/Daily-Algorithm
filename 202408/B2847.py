import sys
input = sys.stdin.readline

N = int(input())
L = []
for _ in range(N):
    L.append(int(input()))

answer = 0
for i in range(N-2, -1, -1):
    if L[i+1] <= L[i]:
        answer += L[i] - L[i+1] + 1
        L[i] = L[i+1] - 1
print(answer)