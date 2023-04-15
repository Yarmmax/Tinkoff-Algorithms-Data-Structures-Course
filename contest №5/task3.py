def find_substrings(s1, s2):
    n, m = len(s1), len(s2)
    counter = 0
    result = []
    for i in range(m - n + 1):
        count_mismatch = 0
        for j in range(n):
            if s1[j] != s2[i+j]:
                count_mismatch += 1
                if count_mismatch > 1:
                    break
        if count_mismatch <= 1:
            counter += 1
            result.append(i+1)
    return counter, result

s1 = input()#'aaaa'
s2 = input()#'Caaabdaaaa'
counter, result = find_substrings(s1, s2)
print(counter)
print(*result)
