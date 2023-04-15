n = int(input())
inp = input()
data = dict()
for i in inp:
    if i not in data:
        data[i] = 0
    data[i] += 1
data = dict(sorted(data.items(), reverse=True))
# print(data)
answer = ""
middle_letter = "a"
for i in data.keys():
    if i < middle_letter and data[i] % 2 != 0:
        middle_letter = i
if middle_letter != "a":
    answer += middle_letter
    data[middle_letter] -= 1
for i in data.keys():
    for __ in range(data[i] // 2):
        answer = i + answer
        answer = answer + i
print(answer)
