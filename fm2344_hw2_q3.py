import math


def factors(num):
    for i in range(1, int(math.sqrt(num) + 1)):
        if num % i == 0:
            yield i
    count = int(math.sqrt(num) - 1)
    while count > 0:
        if num % count == 0:
            yield int(num / count)
        count -= 1


for curr_factor in factors(64):
    print(curr_factor)