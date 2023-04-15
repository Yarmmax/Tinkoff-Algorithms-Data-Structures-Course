n = 4  # int(input())
orders = [1, 2, 3, 4]#[i for i in input().split(" ")]

zero_positions = [0 for i in range(n)]

# ans for orders
for i in range(n):
    zero_positions[orders[i]] = 1
    index = 0
    for j in range(len(zero_positions)-1, 0, -1): # add if for optimize
        if zero_positions[j] == 0:
            index = j
    ans = i+1 + 2 - (n - index) * 2
    print(ans)

