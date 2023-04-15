from collections import Counter

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# создаем словарь частот для каждого числа во втором массиве
freq_b = Counter(b)

# создаем словарь префиксных сумм частот для каждого числа в первом массиве
prefix_freq_a = [Counter()]
for x in a:
    prefix_freq_a.append(prefix_freq_a[-1] + Counter([x]))

# создаем хеш-функцию для множества чисел
def hash_set(s):
    return hash(tuple(sorted(s)))

# ищем наибольший общий подотрезок, являющийся анаграммой
best_len = 0
s1, s2 = set(), set()
for j in range(1, n+1):
    s1.add(a[j-1])
    s2.add(b[j-1])
    if s1 == s2:
        len1 = j
        len2 = j - prefix_freq_a[j][a[j]] + prefix_freq_a[j][a[j]-1]
        if len1 == len2:
            best_len = max(best_len, len1)

    # проверяем оставшиеся возможные пересечения множеств
    if j >= m:
        s1.remove(a[j-m])
        if s1 == s2:
            len1 = j - (j-m) + 1
            len2 = m
            if len1 == len2:
                best_len = max(best_len, len1)

print(best_len)
