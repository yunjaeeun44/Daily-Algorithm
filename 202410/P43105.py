def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            tmp1, tmp2 = 0, 0
            if j-1 >= 0:
                tmp1 = triangle[i-1][j-1]
            if j < i:
                tmp2 = triangle[i-1][j]
            triangle[i][j] += max(tmp1, tmp2)

    return max(triangle[-1])