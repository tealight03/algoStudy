def dfs(graph, node, visited):
    visited[node] = True
    
    for i in graph[node]:
        if visited[i] == False:
            dfs(graph, i, visited)

n = int(input())
m = int(input())

cpt = [[] for i in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for i in range(m):
    a, b = map(int, input().split())
    cpt[a].append(b)
    cpt[b].append(a)

dfs(cpt, 1, visited)

for flag in visited:
    if flag == True:
        cnt += 1

print(cnt-1)