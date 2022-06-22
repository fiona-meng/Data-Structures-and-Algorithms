from random import randint

def split_by_sign(lst, low, high):
    if low >= high:
        return lst
    else:
        if lst[low] > 0 and lst[high] < 0:
            lst[low], lst[high] = lst[high], lst[low]
            return split_by_sign(lst, low+1, high-1)
        elif lst[high] > 0:
            return split_by_sign(lst, low, high - 1)
        elif lst[low] < 0:
            return split_by_sign(lst, low+1, high)


lst = [randint(-10,10) for i in range(10)]
print(lst)
print(split_by_sign(lst, 0, 9))