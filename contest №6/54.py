def f(a, k, m):
    x, y, p, max_val = 0, 0, 0, 0
    for i in range(m):
        x = 0
        for j in range(i + 1, m):
            if a[k][i] <= a[k][j]:
                x += 1
            else:
                break
        y = 0
        for j in range(i, -1, -1):
            if a[k][i] <= a[k][j]:
                y += 1
            else:
                break
        p = a[k][i] * (x + y)
        if p > max_val:
            max_val = p
    return max_val

if __name__ == "__main__":
    n = int(input("Enter a matrix size:\n n = "))
    m = int(input("m = "))
    a = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        row = input().split()
        for j in range(m):
            a[i][j] = int(row[j])
    for j in range(m):
        for i in range(1, n):
            if a[i][j] != 0:
                a[i][j] += a[i-1][j]
    max_val = 0
    for i in range(n):
        if f(a, i, m) > max_val:
            max_val = f(a, i, m)
    print(f"Max square = {max_val}")
