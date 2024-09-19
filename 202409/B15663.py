N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
check = [0 for _ in range(N)]
answer = []

def backtrack():
    if len(answer) == M:
        print(*answer)
    else:
        overlap = 0
        for i in range(0, N):
            if check[i] == 0 and overlap != nums[i]:
                answer.append(nums[i])
                check[i] = 1
                overlap = nums[i]
                backtrack()
                answer.pop()
                check[i] = 0

backtrack()