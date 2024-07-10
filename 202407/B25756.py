import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))

answer = 0
for i in range(N):
    answer = 1 - (1-answer)*(1-L[i]/100)
    print(answer * 100)