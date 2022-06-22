from ArrayStack import ArrayStack


def stack_min(s):
    if len(s) == 1:
        return s.top()
    else:
        val = s.pop()
        result = stack_min(s)

        if val < result:
            result = val
        s.push(val)
        return result


def split_parity(lst, low, high):
    if low == high:
        return lst
    else:
        if lst[low] % 2 != 0 and lst[high] % 2 == 0:
            lst[low], lst[high] = lst[high], lst[low]
        if lst[low] % 2 == 0:
            low += 1
        if lst[high] % 2 != 0:
            high -= 1
        return split_parity(lst, low, high)


# lst1 = [4, -5, 2, 3, -1, -6, 7, 9, 0]
# print(split_parity(lst1, 0, 8))


def nested_sum(lst):
    if isinstance(lst, int):
        return lst
    else:
        total = 0
        for i in lst:
            total += nested_sum(i)
        return total


lst2 = [[1, 2], 3, [4, [5, 6, [7], 8]]]
print(nested_sum(lst2))

