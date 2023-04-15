import sys
sys.setrecursionlimit(1000000)

def dfs(v, c):
    color[v] = c
    comps.append(v+1)
    for u in g[v]:
        if not color[u]:
            dfs(u, c)

n, m = 4, 4
#n, m = map(int, input().split())
inp = [[1, 2], [2, 3], [3, 4], [4, 1]]
g = [[] for i in range(n)]
for i in range(m):
    fr, to = inp[i][0], inp[i][1]
    #fr, to = map(int, input().split())
    g[fr-1].append(to-1)

used = [False for _ in range(n)]

c = 1
res = []
color = [False for _ in range(n)]
for i in range(n):
    if not color[i]:
        comps = []
        dfs(i, c)
        res.append(sorted(comps))
        c += 1

print(res)