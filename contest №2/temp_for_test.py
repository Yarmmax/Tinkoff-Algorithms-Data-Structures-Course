def bub_srt(a, n):
    counter = 0
    for iteration in range(n):
        counter += 1
        had_swaps = False
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                had_swaps = True
        if not had_swaps:
            break
    return counter
# 10 8 9 4 6 3 5 1 11 7 2 while i > i + 1 res = res + 1 else:
add1 = [i for i in [10, 8, 9, 4, 6, 3, 5, 1, 11]]
n = 11
a = [0] * n
for i in add1:
    a[i-1] = 1
print(bub_srt(a, n))