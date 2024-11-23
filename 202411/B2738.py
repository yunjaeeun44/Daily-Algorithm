def add(a, b):
    return a+b

N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split()))) 

answer = []
for i in range(N):
    B = list(map(int, input().split()))
    answer.append(list(map(add, A[i], B)))

for i in range(N):
    print(*answer[i])