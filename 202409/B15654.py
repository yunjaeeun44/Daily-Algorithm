N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [0 for i in range(N)]
ans = []

def backtrack():
    if len(ans) == M:
        print(*ans)
    else:
        for i in range(0, N):
            if visited[i] == 0:
                ans.append(nums[i])
                visited[i] = 1
                backtrack()
                ans.pop()
                visited[i] = 0

backtrack()