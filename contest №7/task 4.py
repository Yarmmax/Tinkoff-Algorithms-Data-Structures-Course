def gen_perm(callback, n, cur, prefix):
    if sum(prefix) == n:
        callback(*prefix)
        return
    for i in range(1, n+1):
        if len(prefix) == 0:
            prefix.append(i)
            flag = gen_perm(callback, n, cur + 1, prefix)
            prefix.pop()
        else:
            if sum(prefix) < n and i <= prefix[-1]:
                prefix.append(i)
                flag = gen_perm(callback, n, cur + 1, prefix)
                prefix.pop()

n = int(input())
gen_perm(print, n, 0, [])