import sys
input = sys.stdin.readline

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)] #T, P
DP = [0] * (N+1)

for i in range(0, N):
    for j in range(i+L[i][0], N+1): 
        DP[j] = max(DP[j], DP[i] + L[i][1])
print(DP[N])