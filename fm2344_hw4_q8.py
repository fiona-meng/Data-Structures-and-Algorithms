

def flat_list(nested_lst, low, high):
    if low == high:
        if isinstance(nested_lst[low], list):
            result = flat_list(nested_lst[low], 0, len(nested_lst[low]) - 1)
        else:
            result = [nested_lst[low]]
    else:
        if isinstance(nested_lst[low], list):
            result = flat_list(nested_lst[low], 0, len(nested_lst[low]) - 1) + flat_list(nested_lst, low + 1, high)
        else:
            result = [nested_lst[low]] + flat_list(nested_lst, low + 1, high)
    return result


nested_lst = [[1, 2], 3, [4, [5, 6, [7, 8, 10], 11]]]
print(flat_list(nested_lst, 0, 2))

