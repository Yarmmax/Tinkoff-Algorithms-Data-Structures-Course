n = int(input())
ord = list(map(int, input().split(" ")))
min_sum = 0
sum_sum = 0
#flag = True
last_zero_ind = n-1
arr = [0] * n
ans = [1]
for i in range(n):
    arr[ord[i]-1] = 1
    #if flag:
    sum_sum += 1
    while arr[last_zero_ind] != 0 and last_zero_ind >= 0:
        last_zero_ind -= 1
        min_sum += 1
        #flag = False
    ans.append(1 + sum_sum - min_sum)
print(*ans)