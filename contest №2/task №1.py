# исправить подсчет инверсий: посмотреть на 1ые элементы и потом уже считать от большего (для чуждого массива элементу!) количество инверсий чтобы его поставить на место

def merge(arr1: tuple, arr2: tuple, counter: int) -> tuple:
    new_arr = list()
    arr1_ptr = 0
    arr2_ptr = 0
    flag = True
    counter = arr1[1] + arr2[1]
    while arr1_ptr != len(arr1[0]) or arr2_ptr != len(arr2[0]):
        if len(arr1[0]) == arr1_ptr:
            new_arr.extend(arr2[0][arr2_ptr:len(arr2[0])])
            break
        if arr2_ptr == len(arr2[0]):
            new_arr.extend(arr1[0][arr1_ptr:len(arr1[0])])
            counter += len(arr1[0]) - arr1_ptr - 1
            break
        if arr1[0][arr1_ptr] < arr2[0][arr2_ptr]:
            new_arr.append(arr1[0][arr1_ptr])
            arr1_ptr += 1
            flag = True
        else:
            # arr1_temp_ptr = arr1_ptr
            arr2_temp_ptr = 0
            while arr1[0][arr1_ptr] > arr2[0][arr2_temp_ptr] and flag == True:
                print(arr1[0][arr1_ptr], "-", arr2[0][arr2_temp_ptr])
                counter += 1
                arr2_temp_ptr += 1
                if arr2_temp_ptr == len(arr2[0]):
                    break
            flag = False
            # counter += 1
            new_arr.append(arr2[0][arr2_ptr])
            arr2_ptr += 1
            # fix flag + arr1[0][0] ??
    return new_arr, counter


def my_sort(arr, n: int, counter):
    if n == 1:
        n = 2
    if len(arr) == 1:
        return arr, counter
    else:
        return merge(my_sort(arr[:n // 2], n // 2, counter), my_sort(arr[n // 2:], n // 2, counter), counter)


def main():
    temp_str = "5 4 3 2 1"  # 5-4 5-3 5-2 5-1 4-3 4-2 4-1 3-2 3-1 2-1
    my_arr = list(map(int, temp_str.split(" ")))
    n = len(my_arr)
    info = my_sort(my_arr, n, 0),
    sorted_arr, counter = info[0][0], info[0][1]
    print(sorted_arr, counter)


if __name__ == "__main__":
    main()
