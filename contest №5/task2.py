# h(s[l,r+1]) = h(s[l, r]) * t + s[r+1]

# ababbababa
# aba
# 0 5 7
# (hr - ((hl *tpow[...]) % mod) + mod) % mod\

def calc_tpow(string, t, mod):
    tpow = [1] * len(string)
    for i in range(1, len(string)):
        tpow[i] = tpow[i-1] * t
        tpow[i] %= mod
    return tpow

def rec_hash(string, tpow):
    if len(string) == 1:
        return ord(string)
    return (((ord(string[0])) * tpow[len(string)] % mod) + rec_hash(string[1:], tpow)) % mod

def hash(string, t, mod, tpow):
    h = 0
    for i in range(len(string)):
        h = (h + (ord(string[i]) - ord('a') + 1) * tpow[len(string)-1-i]) % mod
    return h


def next_hash(s, hash, t, mod, tpow, l):
    prev_hash = ((ord(s[0]) - ord('a') + 1) * tpow[len(s)] + mod) % mod
    next_hash = ((ord(s[-1]) - ord('a') + 1) * tpow[0]) % mod
    _1 = (hash - prev_hash + mod) % mod * t % mod
    _2 = (_1 + next_hash + mod) % mod
    return _2
#curr_hash = ((hash - (ord(haystack[i-1])-ord('a')+1)*tpow) * t + ord(haystack[i+m-1])) % mod
#(hr - ((hl *tpow[...]) % mod) + mod) % mod

t = 31
mod = 1e9+7
string = "ababbababa"
sub = "abc"
#string = input()
#sub = input()
tpow = calc_tpow(string, t, mod)
r = len(sub)
sub_hash = hash(sub, t, mod, tpow)
start_hash = hash(string[:len(sub)], t, mod, tpow)
temp_hash = start_hash
str_hashes = list()
str_hashes.append(temp_hash)
for l in range(len(string)-r+1):
    r += 1
    temp_hash = next_hash(string[l:r], temp_hash, t, mod, tpow, l)
    str_hashes.append(temp_hash)

r = len(sub)
for_check = list()
for l in range(len(string)-r+1):
    for_check.append(hash(string[l:r], t, mod, tpow))
    r += 1

print("for_check: ", for_check)
print("str_hashes: ", str_hashes)
print(sub_hash)

#for i in range(1, n-m+1):
#        curr_hash = ((curr_hash - ord(haystack[i-1])*p_pow) * x + ord(haystack[i+m-1])) % mod
#        if curr_hash == needle_hash and haystack[i:i+m] == needle:
#            res.append(i)

#for i in range(len(str_hashes)):
 #   if str_hashes[i] == sub_hash:
    #    print(i, end=" ")
#