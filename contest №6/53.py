n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
l, r = 1, min(n, m) + 1
x, y = 0, 0
while l < r:
    mean = (l + r) // 2
    flag = False
    for i in range(n):
        ch = 0
        for j in range(m):
            if not A[i][j]:
                ch = 0
            else:
                ch += 1
            if ch >= mean:
                len = mean
                for ii in range(i + 1, min(n, i + mean)):
                    for jj in range(j - mean + 1, j + 1):
                        if 0 <= jj < m and A[ii][jj]:
                            len += 1
                if len == mean * mean:
                    flag = True
                    x, y = j - mean + 2, i + 1
        if flag:
            l = mean + 1
        else:
            r = mean
print(l - 1)
print(x, y)
