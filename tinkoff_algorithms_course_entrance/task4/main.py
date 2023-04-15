limit = int(input())


def calc_am_of_divs(lim):
    amount = 0
    for div in range(1, lim+1):
        if lim % div == 0:
            amount += 1
    return amount


max_amount_of_divs = 0
number = 0
for x in range(1, limit+1):
    temp_am = calc_am_of_divs(x)
    if max_amount_of_divs <= temp_am:
        max_amount_of_divs = temp_am
        number = x
print(number, max_amount_of_divs)
