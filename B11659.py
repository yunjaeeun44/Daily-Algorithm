import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))
prefixSum = [0]
for i in range(1, N+1):
    prefixSum.append(prefixSum[i-1] + nums[i])

for _ in range(M):
    i , j = map(int, input().split())
    print(prefixSum[j] - prefixSum[i-1])