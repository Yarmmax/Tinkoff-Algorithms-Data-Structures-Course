from collections import deque


# 7 3
# 1 3 2 4 5 3 1

def find_mins(d, k):
    result = []
    deq = deque()
    for i in range(len(d)):
        if (len(deq) > 0) and (deq[0] <= i - k):
            deq.popleft()
        while len(deq) > 0 and d[deq[-1]] >= d[i]:
            deq.pop()
        deq.append(i)
        if k - i <= 1:
            result.append(d[deq[0]])
    return result

n, k = list(map(int, input().split()))
data = list(map(int, input().split()))
print(*find_mins(data, k))
