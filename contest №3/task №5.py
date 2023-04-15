n = int(input())
a = list(map(int, input().split()))

# prev[i](t)
prev = [-1] * n
stack = []
for i in range(n):
    while stack and a[stack[-1]] >= a[i]:
        stack.pop()
    if stack:
        prev[i] = stack[-1]
    stack.append(i)

# next
next = [n] * n
stack = []
for i in range(n - 1, -1, -1):
    while stack and a[stack[-1]] >= a[i]:
        stack.pop()
    if stack:
        next[i] = stack[-1]
    stack.append(i)

# maxsum
maxsum = 0
left = -1
right = -1
prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + a[i]
for i in range(n):
    tempsum = a[i] * (prefix_sum[next[i]] - prefix_sum[prev[i] + 1])
    if tempsum > maxsum:
        maxsum = tempsum
        left = prev[i] + 1
        right = next[i] - 1

print(maxsum)