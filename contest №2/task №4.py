n = 3  # int(input())
inp = input()
data = dict()
flag2 = True
for i in inp:
    if i not in data:
        data[i] = 0
    data[i] += 1
    if data[i] > 1:
        flag2 = False
sorted_data = dict(sorted(data.items(), reverse=True))
answer = ""
# print(sorted_data)
temp_data = list()
flag = False
for i in sorted_data.keys():
    if data[i] == 1 or len(sorted_data) == 1:
        temp_data.append(i)
        flag = True
if flag:
    answer += sorted(temp_data)[0]
for i in sorted_data.keys():
    if data[i] > 1:
        for k in range(data[i] // 2):
            answer = i + answer
            answer += i
    if flag2:
        answer = i
print(longest_palindrome(inp))
