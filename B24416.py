N = int(input())
fibs = [0] * (N+1)
fibs[1] = 1
fibs[2] = 1

for i in range(3, N+1):
    fibs[i] = fibs[i-1] + fibs[i-2]

print(fibs[N], N-2)