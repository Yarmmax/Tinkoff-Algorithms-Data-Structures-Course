# base
dp = [1, 1, 1]

n = int(input())

#steps
for i in range(n-1):
    temp = [sum(dp[1:3]), sum(dp), sum(dp)]
    dp = temp
#res
print(sum(dp))