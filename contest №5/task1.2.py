def compute_hashes(s, x):
    n = len(s)
    p = [0] * (n+1)
    p[0] = 1
    for i in range(1, n+1):
        p[i] = p[i-1] * x
    h = [0] * (n+1)
    for i in range(1, n+1):
        h[i] = h[i-1] * x + (ord(s[i-1]) - ord('a') + 1)
    return h, p

def get_substring_hash(h, p, a, b):
    return h[b] - h[a-1] * p[b-a+1]

#s = input()
s = 'a' * 50000
n = len(s)
x = 31
h, p = compute_hashes(s, x)
m = int(input())
for i in range(m):
    a, b, c, d = [1, 25000, 1, 25000] # map(int, input().split())
    if get_substring_hash(h, p, a, b) == get_substring_hash(h, p, c, d):
        print("Yes")
    else:
        print("No")