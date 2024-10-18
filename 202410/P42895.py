def solution(N, number):
    dp = [set() for i in range(10)]
    dp[1].add(N)
    if number == N:
        return 1
    
    for i in range(2, 10):
        dp[i].add(int(str(N)*i))
        for a in range(1, i):
            for j in dp[a]:
                for k in dp[i-a]:
                    dp[i].add(j+k)
                    if j-k>=0: dp[i].add(j-k)
                    if k-j>=0: dp[i].add(k-j)
                    dp[i].add(k*j)
                    if k != 0: dp[i].add(j//k)
                    if j != 0: dp[i].add(k//j)
                    if number in dp[i]:
                        return i
    return -1