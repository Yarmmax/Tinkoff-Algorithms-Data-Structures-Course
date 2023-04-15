#n, m = map(int, input().split())

#dp = [list(map(int, input().split())) for line in range(n)]

#n, m = 3, 5
#dp = [[1, 1, 0, 0, 0,],
      #     [ 1, 1, 1, 1, 1,],
#     [ 0, 0, 0, 1, 1]]


n, m = 5, 5
dp = [[1, 1, 1, 1, 0,],
     [ 1, 1, 1, 0, 1,],
     [ 1, 1, 0, 1, 1,],
     [ 1, 0, 1, 1, 1,],
     [ 0, 1, 1, 1, 1,]]

d = [0 for line in range(m)]
for i in range(n):
    for j in range(m):
        if dp[i][j] == 0:
            d[j] = i
print(d)


