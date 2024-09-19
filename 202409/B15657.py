N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
answer = []

def backtrack(start):
    if len(answer) == M:
        print(*answer)
    else:
        for i in range(start, N):
            answer.append(nums[i])
            backtrack(i)
            answer.pop()

backtrack(0)