amount = int(input())
dataset = list(map(int, input().split()))[::-1]

pad = [0]
_pad = []
end = [0]
res = []

while True:
    _pad.append(dataset.pop())
    while _pad and dataset and _pad[-1] == dataset[-1] + 1:
        _pad.append(dataset.pop())
    if end and dataset and end[-1] + 1 == dataset[-1]:
        _pad.append(dataset.pop())
    res.append((1, len(_pad)))
    pad.extend(_pad)
    _pad = []

    if end[-1] + 1 == pad[-1]:
        _pad.append(pad.pop())
        while _pad[-1] + 1 == pad[-1]:
            _pad.append(pad.pop())

    if _pad:
        res.append((2, len(_pad)))
        end.extend(_pad)
        _pad = []

    if not dataset:
        if _pad:
            res.append((2, len(_pad)))
            end.extend(_pad)
        end.pop(0)
        if end != list(range(1, amount + 1)):
            res = 0
        break
if res == 0:
    print(0)
else:
    print(len(res))
    for a in res:
        print(a[0], a[1])