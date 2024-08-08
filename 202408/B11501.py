import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    
    answer = 0
    maxPrice = 0
    for i in range(len(nums)-1, -1, -1):
        if maxPrice < nums[i]:
            maxPrice = nums[i]
        else:
            answer += maxPrice - nums[i]
    print(answer)