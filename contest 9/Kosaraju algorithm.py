import topsort_realization as tsr


n, m = map(int, input().split())
g = [[] for _ in range(n)]
gr = [[] for _ in range(n)]
for i in range(m):
    fr, to = map(int, input().split())
    g[fr-1].append(to-1)
    gr[to-1].append(fr-1)
#print(g)
#print(gr)
topsort = tsr.topsort(n, m, g, 0)
print(topsort)

color = [0 for _ in range(n)]
g_res = [{} for _ in range(n)]
def unite(v, c):
    color[v] = c
    for u in gr[v]:
        if color[u] == 0:
            unite(u, c)
        elif color[u] != c:
            pass #g_res[color[u]].insert([c])

c = 1
for v in topsort:
    if color[v] == 0:
        unite(v, c)
        c+=1

#print(color)
#print(g_res)
