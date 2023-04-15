n, k = 7, 3 # map(int, input().split(" "))
data = [1, 3, 2, 4, 5, 3, 1]#list(map(int, input().split(" ")))

queue = list()
ans = list()
# 2 [3 4 5] 6 1 -> [2, 3]; 2 < 5 => [3]
temp_min = 0
is_min_calculated = False
for i in range(len(data)):
    if len(queue) < k:
        queue.append(data[i])
    else:
        if not is_min_calculated:
            temp_min = min(queue)
            print(queue.count(temp_min))
            is_min_calculated = True
        if temp_min > data[i]:
            temp_min = data[i]
        queue.append(data[i])
        queue.pop(0)
        ans.append(temp_min)

print(queue)
print(*ans)

# записываем в структуру в одна окна, одно как есть, другое сортируем 