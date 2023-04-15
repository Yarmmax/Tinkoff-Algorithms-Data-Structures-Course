from collections import deque
def bfs(start, end, board):
    dist = [int('inf')] * n
    dist[s] = 0



n = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

board = [[0 for _ in range(n)] for _ in range(n)]

states = [[x1-1, y1-2], [x1-1, y1+2], [x1+1, y1-2], [x1+1, y1+2], [x1-2, y1-1], [x1-2, y1+1], [x1+2, y1+1], [x1+2, y1-1]]

bfs([x1, y1], [x2, y2], board)

print(states)
