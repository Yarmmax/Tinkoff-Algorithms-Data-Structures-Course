amount = int(input())
dataset = list()
for i in range(amount):
    dataset.append(int(input()))
    if dataset[len(dataset)-1] > dataset[len(dataset)-2]:
        #print(dataset[len(dataset)-1], " > ",  dataset[len(dataset)-2])
        dataset[len(dataset) - 1] = dataset[len(dataset) - 2]
for elem in dataset:
    print(elem, end=' ')