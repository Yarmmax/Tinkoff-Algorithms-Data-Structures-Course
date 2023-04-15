def bin_search(arr: list, elem: int) -> int:
    if elem < 1:
        return 0
    l = 0
    r = len(data)
    while l + 1 < r:
        temp = (l+r) // 2
        if elem < arr[temp]:
            r = temp
        else:
            l = temp
    return r


data = list(map(int, input().split(" ")))
for i in range(1, len(data)):
    data[i] = data[i-1] + data[i]
print(data)
x = 0
while x != -1:
    x = int(input())
    print(bin_search(data, x))
