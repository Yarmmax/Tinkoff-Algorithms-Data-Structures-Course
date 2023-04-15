def calc_tpow(s):
    t=31
    mod = 10**9+7
    tpow = [1] * len(s)
    for i in range(1, len(tpow)+1):
        tpow[i] = tpow[i-1] * t % mod
    return tpow

def hash(s, tpow):
    t=31
    mod=10**9+7
    s_hash = 0
    for i in range(len(s)):
        to_plus = (ord(s[i]) - ord('a') + 1) * tpow[i] % mod
        #print(to_plus)
        s_hash += to_plus
    return s_hash


def prefix_hash(s, tpow):
    t = 31
    mod = 10 ** 9 + 7
    pref_hash = [1] * len(s)
    pref_hash[0] = (ord(s[0]) - ord('a') + 1)
    for i in range(1, len(pref_hash)+1):
        pref_hash[i] += pref_hash[i-1] + (ord(s[i]) - ord('a') + 1) * tpow[i] % mod
    return pref_hash

def sub_hash(pref_hash, tpow, l, r):
    t = 31
    mod = 10 ** 9 + 7
    return pref_hash[r+1] - pref_hash[l] * tpow[l-r+1]


s = 'abaaba'
tpow = calc_tpow(calc_tpow(s))
print(tpow)
print(prefix_hash(s, tpow))
#print(sub_hash(prefix_hash(s, tpow), tpow, 3, 6))
