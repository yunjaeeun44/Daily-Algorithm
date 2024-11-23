num = int(input())

dp = [0 for _ in range(num+1)]
dp[0] = 1

for i in range(1, len(dp)):
    dp[i] = dp[i-1]*i
    
print(dp[-1])
