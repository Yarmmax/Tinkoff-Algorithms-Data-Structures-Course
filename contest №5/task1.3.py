def hash(s, x):
    n = len(s)
    p = [0] * (n+1)
    p[0] = 1
    for i in range(1, n+1):
        p[i] = p[i-1] * x
    h = [0] * (n+1)
    for i in range(1, n+1):
        h[i] = h[i-1] * x + (ord(s[i-1]) - ord('a') + 1)
    return h, p

def sub_hash(h, p, a, b):
    return h[b] - h[a-1] * p[b-a+1]

s = input()
n = len(s)
x = 31
h, p = hash(s, x)
m = int(input())
for i in range(m):
    a, b, c, d = map(int, input().split())
    #print(s[a-1:b], s[c-1:d])
    #print(sub_hash(h, p, a, b), sub_hash(h, p, c, d))
    if sub_hash(h, p, a, b) == sub_hash(h, p, c, d):
        print("Yes")
    else:
        print("No")