import sys
input = sys.stdin.readline

N = int(input())
wines = [0] + [ int(input()) for _ in range(N) ]

answer = [0] * (N+1)
answer[0] = 0
answer[1] = wines[1]

if N >= 2:
    answer[2] = wines[1] + wines[2]

if N >= 3:
    answer[3] = max(wines[1] + wines[3], wines[2] + wines[3])
    
if N >= 4:
    for i in range(4, N+1):
        answer[i] = max(answer[i-4]+wines[i-1]+wines[i], answer[i-3]+wines[i-1]+wines[i], answer[i-2]+wines[i])

print(max(answer))