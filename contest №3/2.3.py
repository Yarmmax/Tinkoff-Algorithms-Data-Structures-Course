import heapq

def find_mins(d, k):
    line = [(x, i) for i, x in enumerate(d[:k])]
    heapq.heapify(line)
    yield line[0][0]
    for i, x in enumerate(d[k:], start=1):
        heapq.heappush(line, (x, i+k))
        while line[0][1] <= i-1:
            heapq.heappop(line)
        while line and line[0][0] == d[i-1]:
            heapq.heappop(line)
        if line:
            yield line[0][0]

# k = 3
#data = [1, 3, 2, 4, 5, 3, 1]
n_k = input().split(" ")
n, k = int(n_k[0]), int(n_k[1])
data= list(map(int, input().split(" ")))

for i in find_mins(data, k):
    print(i)