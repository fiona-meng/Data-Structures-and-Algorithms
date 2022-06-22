def permutations(lst, low, high):
    if low == high:
        return [[lst[low]]]
    else:
        result = []
        for i in range(low, high+1):
            value = lst[i]
            r = lst[:i] + lst[i + 1:]
            p = permutations(r, 0, len(r) -1)
            # for j in p:
            #     result.append([value] + j)
        return [value]



lst = [1, 2]
print(permutations(lst, 0, 1))
print([1] + [2])