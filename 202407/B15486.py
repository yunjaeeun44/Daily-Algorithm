import sys
input = sys.stdin.readline

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)] #T, P
DP = [0] * (N+1)

for i in range(N-1, -1, -1):
    if i+L[i][0] > N:
        DP[i] = DP[i+1]
    else:
        DP[i] = max(DP[i+1], L[i][1] + DP[i+L[i][0]])
print(DP[0])