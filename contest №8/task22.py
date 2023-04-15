import sys

sys.setrecursionlimit(1000000)


def dfs(v, flag):
    color[v] = 1
    for u in g[v]:
        if color[u] == 0:
            if dfs(u, flag)[0]:
                return True, flag
        elif color[u] == 1:
            flag = 1
            return True, flag
    color[v] = 2
    return False, flag


n, m = map(int, input().split())
inp = [[1, 2], [2, 3], [3, 4], [4, 1]]
g = [[] for i in range(n)]
for i in range(m):
    fr, to = map(int, input().split())
    g[fr - 1].append(to - 1)

color = [0 for _ in range(n)]
flag = 0
for i in range(n):
    # можно оптимизировать запуская дфс не от всех вершин а предварительно или в процессе выделенных компонент связности
    flag = dfs(i, flag)[1]
    if flag == 1:
        break
print(flag)

