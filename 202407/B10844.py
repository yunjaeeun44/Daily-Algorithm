N = int(input())
DP = []
for _ in range(N+1):
    DP.append([0]*10)
DP[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, N+1):
    DP[i][0] =  DP[i-1][1]
    DP[i][9] =  DP[i-1][8]
    for j in range(1, 9):
        DP[i][j] = DP[i-1][j-1] + DP[i-1][j+1]
        
print(sum(DP[N]) % 1000000000)