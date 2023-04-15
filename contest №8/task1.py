import sys
sys.setrecursionlimit(1000000)

def dfs(v, c):
    color[v] = c
    comps.append(v+1)
    for u in g[v]:
        if not color[u]:
            dfs(u, c)

n, m = 6, 4
#n, m = map(int, input().split()) # 6, 4
inp = [[3, 1], [1, 2], [5, 4], [2, 3]]
g = [[] for i in range(n)]
for i in range(m):
    fr, to = map(int, input().split()) # inp[i][0], inp[i][1]  #
    g[fr-1].append(to-1)
    # g[to-1].append(fr-1)

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

print(len(res))
for i in res:
    print(len(i))
    print(*i)