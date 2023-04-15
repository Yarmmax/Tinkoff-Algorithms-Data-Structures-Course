def calc_res(dataset):
    count_for_vert = 0
    count_for_horz = 0
    for i in dataset:
        # work with vertical figures
        if int(i) == 0:
            if count_for_vert % 2 == 0:
                print(1, 1)
            else:
                print(3, 1)
            count_for_vert += 1
        # work with horizontal figures
        if int(i) == 1:
            if count_for_horz % 4 == 0:
                print(1, 2)
            if count_for_horz % 4 == 1:
                print(2, 2)
            if count_for_horz % 4 == 2:
                print(3, 2)
            if count_for_horz % 4 == 3:
                print(4, 2)
            count_for_horz += 1


inp = input()
calc_res(inp)

