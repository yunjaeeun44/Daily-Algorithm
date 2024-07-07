T = int(input())
DP = [[0, 0] for _ in range(80)]
DP[0] = [1, 0]
DP[1] = [0, 1]
for _ in range(T):
    N = int(input())
    if DP[N] == [0, 0]:
        for i in range(2, N+1):
            DP[i][0] = (DP[i-1][0] + DP[i-2][0])
            DP[i][1] = (DP[i-1][1] + DP[i-2][1])
    print(*DP[N])