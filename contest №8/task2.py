import sys
sys.setrecursionlimit(1000000)

def has_cycle(graph):
    visited = set()
    processed = set()

    def dfs(v):
        visited.add(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                dfs(neighbor)
            elif neighbor not in processed:
                return 1
        processed.add(v)
        return 0

    for vertex in range(len(graph)):
        if vertex not in visited:
            if dfs(vertex):
                return 1

    return 0


n, m = 4, 4
#n, m = map(int, input().split())
inp = [[1, 2], [2, 3], [3, 4], [4, 1]]
g = [[] for i in range(n)]
for i in range(m):
    fr, to = inp[i][0], inp[i][1]
    #fr, to = map(int, input().split())
    g[fr-1].append(to-1)
print(has_cycle(g))

