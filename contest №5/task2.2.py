def calc_tpow(string, t, mod):
    tpow = [1] * len(string)
    for i in range(1, len(string)):
        tpow[i] = tpow[i-1] * t
        tpow[i] %= mod
    return tpow

def hash(string, t, mod, tpow):
    h = 0
    for i in range(len(string)):
        h = (h + (ord(string[i]) - ord('a') + 1) * tpow[len(string)-1-i]) % mod
    return h


t = 31
mod = int(10 ** 9 + 7)

string = input()
sub = input()
tpow = calc_tpow(string, t, mod)
r = len(sub)
sub_hash = hash(sub, t, mod, tpow)
temp_hash = 0
tpow = pow(t, r-1, mod)
for i in range(r):
    temp_hash = (temp_hash + (ord(string[i]) - ord('a') + 1) * pow(t, i, mod)) % mod

if temp_hash == sub_hash and string[:r] == sub:
    print(True)

for i in range(1, len(string) - r + 1):
    temp_hash = (temp_hash - (ord(string[i - 1]) - ord('a') + 1) * tpow) % mod
    temp_hash = (temp_hash * t + (ord(string[i + r - 1]) - ord('a') + 1)) % mod
    if temp_hash == temp_hash and string[i:i + r] == sub:
        print(True)
print(False)