import sys
input = sys.stdin.readline

N = int(input())
stairs = [0]
for _ in range(N):
    stairs.append(int(input()))
    
DP = [0, stairs[1]]
if N > 1:
    DP.append(stairs[1]+stairs[2])
    for i in range(3, N+1):
        DP.append(max(DP[i-2]+stairs[i], DP[i-3]+stairs[i-1]+stairs[i]))
print(DP[N])