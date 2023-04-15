limit = int(input())
dataset = [i for i in range(1, limit+1)]
if sum(dataset) % 3 == 0:
    lim = int(sum(dataset) / 3)
    blacklist = list()
    for i in range(3):
        temp = []
        sum_of_subset = 0
        counter = len(dataset) - 1
        while sum_of_subset != lim:
            if sum_of_subset + dataset[counter] <= lim and not(dataset[counter] in blacklist):
                temp.append(dataset[counter])
                blacklist.append(dataset[counter])
                sum_of_subset += dataset[counter]
            counter -= 1
        print(len(temp))
        for elem in temp:
            print(elem, end=' ')
        print("\n")
else:
    print(-1)
