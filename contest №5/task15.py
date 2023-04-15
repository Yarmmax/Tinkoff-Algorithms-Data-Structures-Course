s = input()
n = int(input())
mod = 100000007
t = 31
tpow = [1]
pref_hash = [0]
for i in range(len(s)):
    pref_hash.append((pref_hash[i] * t + ord(s[i])) % mod)
for i in range(len(s)):
    tpow.append((tpow[i] * t) % mod)
for i in range(n):
    a, b, c, d = map(int, input().split())
    if (pref_hash[b] - pref_hash[a-1] * tpow[b - a + 1] + mod) % mod == (pref_hash[d] - pref_hash[c-1] * tpow[d - c + 1] + mod) % mod:
        print("Yes")
    else:
        #print(pref_hash[b] - pref_hash[a-1] * tpow[b - a - 1])
        #print(pref_hash[d] - pref_hash[c-1] * tpow[d - c - 1])
        print("No")
