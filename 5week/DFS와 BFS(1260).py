def dfs(graph, node, visited):
    visited[node] = True
    print(node, end = " ")
    
    for i in graph[node]:
        if visited[i] == False:
            dfs(graph, i, visited)

def bfs(graph, node, visited):
    queue = [node]
    visited[node] = True

    while queue:
        node = queue.pop(0)
        print(node, end = " ")

        for i in graph[node]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())
graph = []

for _ in range(n+1):
    graph.append([])

visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

dfs(graph, v, visited)
print()

visited = [False] * (n+1)
bfs(graph, v, visited)