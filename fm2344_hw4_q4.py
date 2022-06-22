from random import randint

def list_min(lst, low, high):
    if low == high:
        return lst[low]
    else:
        result = list_min(lst, low + 1, high)
        if result > lst[low]:
            return lst[low]
        else:
            return result


def main():
    lst = [randint(-100, 100) for i in range(10)]
    print(lst)
    print(list_min(lst, 0, 9))

main()