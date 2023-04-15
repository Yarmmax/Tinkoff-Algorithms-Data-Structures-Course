def main():
    import sys

    def query(x):
        print(x)
        sys.stdout.flush()
        return input()

    left = 0
    right = int(input()) + 1
    shift = 1
    info = list()
    while left + 1 < right:
        shift = (left + right) // 2
        if query(shift) == ">=":
            info.append(">=")
            left = shift
        else:
            info.append("<")
            right = shift
    if info[len(info)-1] == "<":
        print("! " + str(shift-1))
    else:
        print("! " + str(shift))


if __name__ == '__main__':
    main()
