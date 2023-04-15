# import time


def find_intervals(lim: float):
    x = 1
    while x ** 2 + (x + 1) ** 0.5 <= lim:
        x *= 2
    if x > 10000000000:
        x = 10000000000
    return x // 2, x


def find_solution(intervals: set, const: float):
    left = intervals[0]
    right = intervals[1]
    shift = left
    counter = 0
    while round(shift ** 2 + (shift + 1) ** 0.5, 6) != const:
        counter += 1
        # print(round(shift ** 2 + (shift + 1) ** 0.5, 6))
        shift = (left + right) / 2
        if shift ** 2 + (shift + 1) ** 0.5 < const:
            left = shift
        else:
            right = shift
        if counter > 1000:
            break
    return shift


def main():
    c = float(input())
    # start = time.time()  ## точка отсчета времени
    print(find_solution(find_intervals(c), c))
    # end = time.time() - start  ## собственно время работы программы
    # print(end)  ## вывод времени


if __name__ == '__main__':
    main()
