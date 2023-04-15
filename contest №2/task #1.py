def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left_part, left_counter = merge_sort(arr[:mid])
    right_part, right_counter = merge_sort(arr[mid:])
    new_arr = []
    left_ptr = 0
    right_ptr = 0
    merge_counter = 0
    while left_ptr < len(left_part) and right_ptr < len(right_part):
        if left_part[left_ptr] <= right_part[right_ptr]:
            new_arr.append(left_part[left_ptr])
            left_ptr += 1
        else:
            new_arr.append(right_part[right_ptr])
            right_ptr += 1
            merge_counter += len(left_part) - left_ptr
    new_arr += left_part[left_ptr:] + right_part[right_ptr:]
    inv_amount = left_counter + merge_counter + right_counter
    return new_arr, inv_amount


def main():
    n = int(input())
    inp_arr = list(map(int, input().split(" ")))
    sorted_arr, inv_counter = merge_sort(inp_arr)
    print(inv_counter)
    print(' '.join(map(str, sorted_arr)))


if __name__ == "__main__":
    main()
