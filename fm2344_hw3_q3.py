from random import randint
def find_duplicates(lst):
    duplicate_list = []
    for i in range(len(lst)):
        index = lst[i] % len(lst)
        lst[index] += len(lst)
    for i in range(len(lst)):
        if lst[i] >= 2*(len(lst)):
            duplicate_list.append(i)

    return duplicate_list


def main():
    lst = [randint(0,7) for i in range(8)]
    print(lst)
    print(find_duplicates(lst))


