def solution(m, n, puddles):
    map = [[0]*m for i in range(n)]
    map[0][0] = 1

    for i in range(n):
        for j in range(m):
            if [j+1, i+1] in puddles:
                continue
            if i-1 >= 0: map[i][j] += map[i-1][j]
            if j-1 >= 0: map[i][j] += map[i][j-1]

    return map[-1][-1] % 1000000007