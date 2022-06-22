def sum_square(n):
    result = 0
    counter = n-1
    while counter > 0:
        result += counter ** 2
        counter -= 1
    return result


sum([(i + 1) ** 2 for i in range(n - 1)])


def sum_odd_square(n):
    result = 0
    counter = n - 1
    while counter > 0:
        if counter % 2 != 0:
            result += counter ** 2
        counter -= 1
    return result

sum([(i + 1)**2 for i in range(n - 1) if (i+1) % 2 != 0])

