N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]
ans = []

def backtrack(start):
    if len(ans) == M:
        print(*ans)
        
    else:
        for i in range(start, N):
            ans.append(nums[i])
            backtrack(i+1)
            ans.pop()

backtrack(0)