n, m = map(lambda x: int(x)+2, input().split())

#base
dp = [[0] * (m+3) for _ in range(n+3)]
dp[2][2], i, j = 1, 2, 2

#steps
while i != n-1 or j != m-1:
    x = i
    y = j
    while x >= 2 and y < m:
        #step
        dp[x][y] += dp[x+1][y-2] + dp[x-1][y-2] + dp[x-2][y-1] + dp[x-2][y+1]
        x -= 1
        y += 1
    if i == n-1:
        j += 1
    else:
        i += 1

#res
dp[n-1][m-1] += dp[n][m-3] + dp[n-2][m-3] + dp[n-3][m-2] + dp[n-3][m]
print(dp[n-1][m-1])

