import sys
input = sys.stdin.readline

nums1 = set([i for i in range(1, 31)])
nums2 = []
for i in range(28):
    nums2.append(int(input()))
    
answer = nums1 - set(nums2)
print(min(answer))
print(max(answer))