n, m = map(int, input().split())

pd = [list(map(int, input().split())) for line in range(n)]
#n, m = 3, 5
#pd = [[1, 1, 0, 0, 0,],
#[1, 1, 1, 1, 1,],
#[0, 0, 0, 1, 1]]

#print(pd)

def update(pd, i, j, n, m):
    line_counter = 0
    for k in range(i, n):
        if pd[k][j] != 0:
            line_counter += 1
        else:
            break
    column_counter = 0
    for k in range(j, m):
        if pd[i][k] != 0:
            column_counter += 1
        else:
            break
    if column_counter == line_counter:
        return line_counter
    return pd[i][j]

x, y = 0, 0
max = 0
max_square = 0
for i in range(n):
    for j in range(m):
        temp = update(pd, i, j, n, m)
        if temp >= max:
            max = temp
            x, y = i, j
print(max)
print(x+1, y+1)

