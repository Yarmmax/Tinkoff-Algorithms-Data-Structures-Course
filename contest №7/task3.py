def calc_sub(arr):
    sub = 1
    for i in range(len(arr)):
        sub *= arr[i]
    return sub

def find_subs(callback, n, cur, prefix, F, counter):
    if calc_sub(prefix) == n:
        counter += 1
        #callback(*prefix)
        return counter

    # отсечение
    if calc_sub(prefix) >= n:
        return counter

    for i in range(len(F)):
        if calc_sub(prefix) * F[i] <=n:
        #if  F[i] <= n:
            if len(prefix) == 0:
                prefix.append(F[i])
                counter = find_subs(callback, n, cur + 1, prefix, F, counter)
                prefix.pop()
            else:
                if calc_sub(prefix) < n and F[i] >= prefix[-1]:
                 prefix.append(F[i])
                 counter = find_subs(callback, n, cur + 1, prefix, F, counter)
                 prefix.pop()
        else:
            return counter
            #break


n = int(input())
F = [1, 1]
temp = 0
while temp < 1e+9:
    temp = F[-1] + F[-2]
    F.append(temp)
F.remove(1)
F.remove(1)
#print(F)

for _ in range(1, n+1):
    num = int(input())
    print(find_subs(print, num, 0, [], F, 0))