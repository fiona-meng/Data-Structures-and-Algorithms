from random import randint
def split_parity(lst):
    last_even = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 1:
            lst[i], lst[last_even] = lst[last_even], lst[i]
            last_even += 1
    return lst


def main():

    lst = [randint(-10, 10) for i in range(10)]
    print(split_parity(lst))

main()




