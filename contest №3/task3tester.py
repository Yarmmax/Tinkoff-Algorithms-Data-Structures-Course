import random
from queue import Queue
from queue import LifoQueue


test_amount = 10000
inp_of_test = list()
data = list()
for _ in range(test_amount):
    ans1 = list()
    ans2 = list()
    inp_of_test = list()
    amount = random.randint(1, 30)
    dataset = random.sample( [i for i in range(1, amount+1)],amount)
    stack_end = list()
    stack_pad = list()
    global_action_counter = 0
    answer = list()
    local_action_counter1 = 0
    local_action_counter2 = 0
    is_possible = True
    is_end_empty = True
    is_pad_empty = True
    counter = 0
    while counter < amount:
        if len(stack_end) == 0 or stack_end[-1] > dataset[counter]:
            stack_end.append(dataset[counter])
            local_action_counter1 += 1
            counter += 1
        else:
            global_action_counter += 1
            answer.append(1)
            answer.append(local_action_counter1)
            local_action_counter1 = 0
            if not is_pad_empty:
                if stack_end[-1] != len(stack_pad) + 1:
                    is_possible = False
                    break
                while len(stack_end) != 0 and stack_pad[-1] + 1 == stack_end[-1]:
                    stack_pad.append(stack_end.pop())
                    local_action_counter2 += 1
                if len(stack_end) == 0:
                    is_end_empty = True
                # local_action_counter2 += 1
            if is_pad_empty:
                if stack_end[-1] != len(stack_pad) + 1:
                    is_possible = False
                    break
                else:
                    is_pad_empty = False
                    stack_pad.append(stack_end.pop())
                    local_action_counter2 += 1
                    while len(stack_end) != 0 and stack_pad[-1] + 1 == stack_end[-1]:
                        stack_pad.append(stack_end.pop())
                        local_action_counter2 += 1
                    if len(stack_end) == 0:
                        is_end_empty = True
            answer.append(2)
            answer.append(local_action_counter2)
            local_action_counter2 = 0
            global_action_counter += 1
    answer.append(1)
    answer.append(local_action_counter1)
    global_action_counter += 1
    answer.append(2)
    answer.append(len(stack_end))
    global_action_counter += 1
    if is_possible:
        #print(global_action_counter)
        for j in answer:
            ans1.append(j)
    else:
        ans1.append(0)


    ####

    #_ = input()
    A1 = dataset#list(map(int, input().split()))
    N = len(A1)

    A1 = A1[::-1]

    T = [0]
    t = []  # вспомогательный
    A2 = [0]
    res = []

    while 1:
        t.append(A1.pop())
        while t and A1 and t[-1] == A1[-1] + 1:
            t.append(A1.pop())
        if A2 and A1 and A2[-1] + 1 == A1[-1]:
            t.append(A1.pop())
        res.append((1, len(t)))
        T.extend(t)
        t = []

        if A2[-1] + 1 == T[-1]:
            t.append(T.pop())
            while t[-1] + 1 == T[-1]:
                t.append(T.pop())

        if t:
            res.append((2, len(t)))
            A2.extend(t)
            t = []

        if not A1:
            if t:
                res.append((2, len(t)))
                A2.extend(t)
            A2.pop(0)
            if A2 != list(range(1, N + 1)):
                res = 0
            break
    if res == 0:
        ans2.append(0)
    else:
        for a in res:
            global_action_counter += 1
            print(a[0])
            print(a[1])

    #print(dataset)
    #print(ans1)
    #print(ans2)
    if ans1 == ans2:
        data.append(1)
    else:
        data.append(0)
        data.append(dataset)
        data.append(ans1)
        data.append(ans2)
    ####
flag = True
for i in range(len(data)):
    if data[i] == 0:
       print("Нашёл!", data[i+1], data[i+2], data[i+3], sep="\n")
       flag = False
       break
if flag == True:
    print("Всё ок!")