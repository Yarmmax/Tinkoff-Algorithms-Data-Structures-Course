def damlev(s, t):
    n = len(s)
    m = len(t)
    infinity = n + m
    D = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(n + 1):
        D[i][0] = i
    for j in range(m + 1):
        D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                cost = 0
            else:
                cost = 1
            D[i][j] = min(D[i - 1][j] + 1,  D[i][j - 1] + 1,  D[i - 1][j - 1] + cost)
            if i > 1 and j > 1 and s[i - 1] == t[j - 2] and s[i - 2] == t[j - 1]:
                D[i][j] = min(D[i][j], D[i - 2][j - 2] + cost)
    return D[n][m]

str1 = input()
str2 = input()
print(damlev(str1, str2))




