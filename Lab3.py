from math import floor


def reverse_list(lst, low = None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = 0
    while low < high:
        lst[low], lst[high] = lst[high], lst[low]
        low += 1
        high -= 1
    return lst

def reverse_list_v2(lst):
    for i in range(0, len(lst)//2):
        lst[i], lst[len(lst)-1-i] = lst[len(lst) - 1 -i], lst[i]
    return lst

    # interval = high - low
    # for i in range(floor(interval/2)):
    #     x = lst[low]
    #     y = lst[high]
    #     lst[low] = y
    #     lst[high] = x
    #     low += 1
    #     high -= 1
    # return lst

lst1 = [1, 2, 3, 4, 5, 6]
print(reverse_list_v2(lst1))


def move_zeros(nums):
    last_zero = 0  #keep track of last zero
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[last_zero] = nums[last_zero], nums[i]
            last_zero += 1
    return nums

lst = [0, 1, 0, 3, 13, 0]
lst1 = [0, 0, 0, 1, 13, 3]
lst2 = [1, 13, 3, 0, 0, 0]
print(move_zeros(lst))
print(move_zeros(lst2))


# lst=[1, 2, 3, 4, 5, 6] reverse whole list -> [6, 5, 4, 3, 2, 1]
# reverse list from 0 to k-1 [5, 6, 4, 3, 2, 1]
# reverse list from k to len(lst) -1 -> [5, 6, 1, 2, 3, 4]

def shift(lst, k):
    reverse_list(lst)
    reverse_list(lst, 0, k-1)
    reverse_list(lst, k, len(lst)-1)

# reverse whole list cost n
# reverse list from 0 to k-1 cost k
# reverse list from k to n cost n-k
# together n+k-1+n-k = 2n


def findMaxAverage(nums, k):
    average = []
    _sum, start = 0, 0
    for end in range(len(nums)):
        _sum += nums[end]

        if end >= k - 1:
            average.append(_sum / k)
            _sum -= nums[start]
            start += 1
    return max(average)

# print(findMaxAverage([1, 12, -5, -6, 50, 3], 2))


def example1(lst):
    n = len(lst)
    total = 0
    for j in range(n):
        for k in range(1+j):
            total += lst[k]
    return total
print(example1([1, 2, 3]))



def my_reverse(lst, low, high):
    while low < high:
        lst[low], lst[high] = lst[high], lst[low]
        low += 1
        high -= 1
    return lst

my_list = [1, 2, 3, 4, 5, 6]
print(my_reverse(my_list, 0, 5))




