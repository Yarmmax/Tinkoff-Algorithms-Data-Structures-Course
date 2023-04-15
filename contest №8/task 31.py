from collections import deque
def bfs(start, end, n):
    neighbors = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

    queue = deque([start])

    came_from = {start: None}

    while queue:
        node = queue.popleft()
        for neighbor in neighbors:
            x = node[0] + neighbor[0]
            y = node[1] + neighbor[1]
            if 1 <= x <= n and 1 <= y <= n and (x, y) not in came_from:
                queue.append((x, y))
                came_from[(x, y)] = node
                if (x, y) == end:
                    path = [end]
                    while end in came_from:
                        end = came_from[end]
                        path.append(end)
                    return path[::-1]
    return None

n = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

start = (x1, y1)
end = (x2, y2)

path = bfs(start, end, n)
path.remove(None)
print(len(path) - 1)
for p in path:
    print(p[0], p[1])
