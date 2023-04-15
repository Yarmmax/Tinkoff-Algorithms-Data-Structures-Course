from collections import deque

K = int(input())

Q = deque([1])
dist = [-1] * K
dist[1 % K] = 1

while Q:
    x = Q.popleft()
    for r in range(K):
        y = (x * 10 + r) % K
        if dist[y] == -1:
            Q.append(y)
            dist[y] = dist[x] + r

print(dist[0])
