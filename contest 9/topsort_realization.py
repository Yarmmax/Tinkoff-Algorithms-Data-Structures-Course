def topsort(n, m, g, start):

    def dfs(v):
        used[v] = True
        for u in g[v]:
            if not used[int(u)]:
                dfs(u)
        topsort.append(v)

    topsort = []
    used = [False] * n
    dfs(start)
    return topsort[::-1]


# n, m = map(int, input().split())
# g = [[] for _ in range(n)]
# gr = [[] for _ in range(n)]
# for i in range(m):
#     fr, to = map(int, input().split())
#     g[fr-1].append(to-1)
#     gr[to-1].append(fr-1)
# print(topsort(n, m, g, 0))



