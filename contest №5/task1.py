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

def sub_hash(s_hash, t):
    return 

t = 31
mod = int(10 ** 9 + 7)
string = 'a' * 50000
#string = input()
n = int(input())
tpow = calc_tpow(string, t, mod)
string_hash = hash(string, t, mod, tpow)
answer = list()
for i in range(n):
    #info = list(map(int, input().split()))
    info = [1, 25000, 1, 25000]
    if info[1] - info[0] == info[3] - info[2]:
        hash1 = hash(string[info[0]-1:info[1]], t, mod, tpow)
        hash2 = hash(string[info[2]-1:info[3]], t, mod, tpow)
        if hash1 == hash2 and string[info[0]:info[1]] == string[info[2]:info[3]]:
            answer.append("Yes")
        else:
            answer.append("No")
    else:
        answer.append("No")
print(answer)
#print(string[info[0]-1:info[1]])