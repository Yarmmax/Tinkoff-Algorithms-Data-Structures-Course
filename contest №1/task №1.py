def bin_search(elem: int, arr: list) -> bool:
    left = 0
    right = len(arr)
    while left + 1 < right:
        temp = (left + right) // 2
        if arr[temp] > elem:
            right = temp
        elif arr[temp] < elem:
            left = temp
        else:
            return True
    if elem == arr[0]:
        return True
    return False


def main():
    n, k = map(int, input().split(" "))
    data = list(map(int, input().split(" ")))
    digits = list(map(int, input().split(" ")))
    for i in digits:
        if bin_search(i, data):
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()
