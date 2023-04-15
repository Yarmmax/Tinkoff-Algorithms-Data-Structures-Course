n, m = map(int, input().split())

#base

string = [0] * (n + 3)
dp = []
for _ in range(m + 3):
    dp.append(string.copy())
dp[2][2] = 1
# print(string)
# print(dp)


# step
for i in range(2, m+2):
    for j in range(2, n+2):
        dp[i][j] += dp[i+1][j-2] + dp[i-1][j-2] + dp[i-2][j-1] + dp[i-2][j+1]
        print(i, j)

# result
print(dp[m+1][n+1])
