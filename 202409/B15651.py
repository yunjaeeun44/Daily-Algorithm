N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]
ans = []

def backtrack():
    if len(ans) == M:
        print(*ans)
    else:
        for i in nums:
            ans.append(i)
            backtrack()
            ans.pop()

backtrack()