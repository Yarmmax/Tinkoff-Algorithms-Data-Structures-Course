def find_gap(arr: list) -> set:
    const = data[0]
    l = 0
    r = len(data)
    while r - l > 1:
        temp = (l + r) // 2
        check = data[temp]
        if check < const:
            r = temp
        else:
            l = temp
    return l


def bin_search(arr: list, elem: int) -> int:
    left = 0
    right = len(arr)
    while right - left > 1:
        shift = (left + right) // 2
        if arr[shift] <= elem:
            left = shift
        else:
            right = shift

    if arr[left] == elem:
        return left
    else:
        return -1


data = list(map(int, input().split(" ")))
gap_pos = find_gap(data)
x = int(input())
if bin_search(data[:gap_pos+1], x) == -1:
    print(len(data[:gap_pos+1]) + bin_search(data[gap_pos+1:], x))
else:
    print(bin_search(data[:gap_pos+1], x))
