# import time


def find_intervals(coefs: list):
    x = 1
    a, b, c, d = map(int, coefs)
    temp = 1
    if a * x ** 3 + b * x ** 2 + c * x + d > 0:
        if a < 0:
            while a * x ** 3 + b * x ** 2 + c * x + d > 0:
                x += temp
                temp *= 2
            return x - temp, x
        if a > 0:
            while a * x ** 3 + b * x ** 2 + c * x + d > 0:
                x -= temp
                temp *= 2
            return x, x + temp
    else:
        if a > 0:
            while a * x ** 3 + b * x ** 2 + c * x + d < 0:
                x += temp
                temp *= 2
            return x - temp, x
        else:
            while a * x ** 3 + b * x ** 2 + c * x + d < 0:
                x -= temp
                temp *= 2
            return x, x + temp


def find_solution(intervals: set, coefs: list):
    a, b, c, d = map(int, coefs)
    left = intervals[0]
    right = intervals[1]
    shift = left
    counter = 0
    if a > 0:
        while round(a * shift ** 3 + b * shift ** 2 + c * shift + d, 64) != 0:
            counter += 1
            # print(round(shift ** 2 + (shift + 1) ** 0.5, 6))
            shift = (left + right) / 2
            if a * shift ** 3 + b * shift ** 2 + c * shift + d < 0:
                left = shift
            else:
                right = shift
            if counter > 100000:
                break
    else:
        while round(a * shift ** 3 + b * shift ** 2 + c * shift + d, 64) != 0:
            counter += 1
            # print(round(shift ** 2 + (shift + 1) ** 0.5, 6))
            shift = (left + right) / 2
            if a * shift ** 3 + b * shift ** 2 + c * shift + d > 0:
                left = shift
            else:
                right = shift
            if counter > 100000:
                break
    return shift


def main():
    abcd = list(map(int, input().split(" ")))
    # start = time.time()  ## точка отсчета времени
    print(find_solution(find_intervals(abcd), abcd))
    # print(find_intervals(abcd))
    # end = time.time() - start  ## собственно время работы программы
    # print(end)  ## вывод времени


if __name__ == '__main__':
    main()
