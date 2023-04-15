import sys
sys.setrecursionlimit(1000000)


from collections import defaultdict

n, m, s, t = map(int, input().split())
graph = defaultdict(list)
for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dist = [float('inf')] * (n + 1)
dist[s] = 0

visited = [False] * (n + 1)
order = []

def dfs(u):
    visited[u] = True
    for v, w in graph[u]:
        if not visited[v]:
            dfs(v)
    order.append(u)

for u in range(1, n + 1):
    if not visited[u]:
        dfs(u)

order.reverse()

for u in order:
    for v, w in graph[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w

if dist[t] == float('inf'):
    print("Unreachable")
else:
    print(dist[t])
