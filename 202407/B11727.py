N = int(input())
DP = [0] * (N+2)
DP[1] = 1
DP[2] = 3

if N > 2:
    for i in range(3, N+1):
        DP[i] = DP[i-1] + DP[i-2]*2

print(DP[N]%10007)