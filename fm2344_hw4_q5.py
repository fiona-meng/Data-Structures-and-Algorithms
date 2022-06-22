def count_lowercase(s, low, high):
    if low == high:
        if s[low].islower():
            return 1
        else:
            return 0
    else:
        if s[low].islower():
            return 1 + count_lowercase(s, low+1, high)
        else:
            return count_lowercase(s, low+1, high)

# s = "aaaaaaaaa"
# print(count_lowercase(s, 0, 8))

def is_number_of_lowercase_even(s, low, high):
    if low == high:
        if s[low].islower():
            return False
        else:
            return True
    else:
        if s[low].islower():
            return (1 + count_lowercase(s, low+1, high))% 2 == 0
        else:
            return count_lowercase(s, low+1, high) % 2 == 0

# s = "A"
# print(is_number_of_lowercase_even(s, 0, 0))
