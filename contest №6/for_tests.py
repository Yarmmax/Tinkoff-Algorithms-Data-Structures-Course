n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]

ans = 0
d = [-1] * m
d1, d2 = [0] * m, [0] * m
st = []
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            d[j] = i
    st.clear()
    for j in range(m):
        while st and d[st[-1]] <= d[j]:
            st.pop()
        d1[j] = st[-1] if st else -1
        st.append(j)
    st.clear()
    for j in range(m - 1, -1, -1):
        while st and d[st[-1]] <= d[j]:
            st.pop()
        d2[j] = st[-1] if st else m
        st.append(j)
    for j in range(m):
        ans = max(ans, (i - d[j]) * (d2[j] - d1[j] - 1))

print(ans)
