n = int(input())
a = [i for i in range(1, n+1)]

if n == 1:
    print(1)
else:
    for i in range(2, n):
        a[i//2], a[i] = a[i], a[i//2]
    print(*a)