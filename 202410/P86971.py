def dfs(a, graph, visited):
    visited[a] = 1
    for x in graph[a]:
        if visited[x] == 0:
            dfs(x, graph, visited)
    
    
def solution(n, wires):
    graph = [[] for i in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    answer = 100
    for wire in wires:
        visited = [0 for i in range(n+1)]
        a, b = wire

        visited[b] = 1 #a의 목적지인 b는 가면 안되므로 1로 지정
        dfs(a, graph, visited)
        cnt = sum(visited) - 1
        answer = min(answer, abs(cnt - (n-cnt)))
        print("cnt", cnt, n-cnt)
    

    return answer