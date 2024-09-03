import sys 
input = sys.stdin.readline

T = int(input())
DP = [0, 1, 2, 4]

for _ in range(T):
    N = int(input())
    for i in range(len(DP), N+1):
        DP.append((DP[i-1] + DP[i-2] + DP[i-3]) % 1000000009)
    print(DP[N] % 1000000009)