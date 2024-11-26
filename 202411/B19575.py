import sys
input = sys.stdin.readline

N, X = map(int, input().split())
answer = 0
for _ in range(N+1):
    A, i = map(int, input().split())
    if i:
        answer = (answer+A)*X
    else:
        answer += A
    answer %= 1000000007

print(answer)