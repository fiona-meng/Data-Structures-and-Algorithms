def sum_to(n):
    result = 0
    if(n==0):
        result += 0
    else:
        result = n + sum_to(n-1)
    return result


def product_evens(n):
    result = 1
    if 2 >= n:
        result = result * 2
    else:
        result = n * product_evens(n-2)
    return result


def find_max(lst, low, high):
    if (low ==high):
        return lst[0]
    else:
        prev = find_max(lst, low+1, high)
        if prev > lst[0]:
            return prev
        else:
            return lst[0]

lst = [13, 9, 16, 3, 4, 2]
print(find_max(lst, 0, 5))
print(True & False)
