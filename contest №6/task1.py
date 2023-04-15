n = int(input())
# base dp[0] = 0    dp[1] = cost of 1st step
dp = [0] + list(map(int, input().split()))

# move and count min sum for each step
for i in range(2, len(dp)):
    dp[i] = dp[i] + min(dp[i-1], dp[i-2])
print(dp[-1])
