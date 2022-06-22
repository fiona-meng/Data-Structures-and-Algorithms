def fibs(n):
    x = 1
    yield x
    y = 1
    yield y
    for i in range(n-2):
        z = x + y
        x = y
        y = z
        yield z

for curr in fibs(8):
    print(curr)
