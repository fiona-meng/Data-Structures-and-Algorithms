# def remove_all(lst, value):
#     end = False
#     while (end == False):
#         try:
#             lst.remove(value)
#         except ValueError:
#             end = True

from random import randint
def remove_all(lst, value):
    last_val = 0
    x = len(lst)
    for i in range(x):
        if lst[i] != value:
            lst[i], lst[last_val] = lst[last_val], lst[i]
            last_val += 1

    for j in range(last_val, x):
        lst.pop()
    return lst


def main():
    lst = [randint(-5, 5)for i in range(10)]
    print(lst)
    val = randint(-5,5)
    print(val)
    remove_all(lst, val)
    print(lst)



