#크루스칼 알고리즘
def solution(n, costs):
    costs.sort(key = lambda x: x[2])
    parents = [[i] for i in range(n)]
    
    answer = 0
    for a, b, cost in costs:
        if parents[a] != parents[b]:
            answer += cost
            tmp = parents[b]
            for i in range(n):
                if parents[i] == tmp:
                    parents[i] = parents[a]
    return answer