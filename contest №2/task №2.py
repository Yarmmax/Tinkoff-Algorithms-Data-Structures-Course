def make_test(arr, n):
    for i in range(2, n):
        arr[i], arr[i // 2] = arr[i // 2], arr[i]
    return arr

def main():
    n = int(input())
    arr = [i+1 for i in range(n)]
    print(*make_test(arr, n))

if __name__ == "__main__":
    main()
