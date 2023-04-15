def bin_search(elem: int, arr: list) -> int:
    left = 0
    right = len(arr)
    while right - left > 1:
        shift = (left + right) // 2
        if arr[shift] <= elem:
            left = shift
        else:
            right = shift
    return left


def find_the_nearest(elem: int, pos: int, arr: list) -> int:
    if len(arr) == 1:
        return arr[0]
    if len(arr) - 1 == pos:
        return arr[pos]
    if abs(arr[pos] - elem) <= abs(arr[pos+1] - elem):
        return arr[pos]
    else:
        return arr[pos+1]


def main():
    n, k = map(int, input().split(" "))
    data = list(map(int, input().split(" ")))
    digits = list(map(int, input().split(" ")))
    for i in digits:
        print(find_the_nearest(i, bin_search(i, data), data))


if __name__ == '__main__':
    main()
