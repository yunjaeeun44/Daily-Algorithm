N = int(input())
L = list(map(int, input().split()))
DP = [0] * N
DP[0] = L[0]

for i in range(1, N):
    for j in range(i):
        if L[j] < L[i]:
            DP[i] = max(DP[i], DP[j] + L[i])
        else:
            DP[i] = max(DP[i], L[i])
print(max(DP))