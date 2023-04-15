def hash(s):
    return sum(s)

def next_hash(hash, n, p):
    return hash + n - p


def is_anagram(a, b):
    a_dict = {}
    b_dict = {}
    for x in a:
        a_dict[x] = a_dict.get(x, 0) + 1
    for x in b:
        b_dict[x] = b_dict.get(x, 0) + 1
    return a_dict == b_dict

def find_max_anagram_subarray(a, b):
    n = len(a)
    m = len(b)
    max_len = 0
    for i in range(n):
        for j in range(i, n):
            subarray = a[i:j+1]
            subarray_hash = generate_hash(subarray)
            for k in range(m):
                if k + len(subarray) <= m:
                    if generate_hash(b[k:k+len(subarray)]) == subarray_hash:
                        if is_anagram(subarray, b[k:k+len(subarray)]):
                            max_len = max(max_len, len(subarray))
    return max_len

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

print(find_max_anagram_subarray(a, b))
