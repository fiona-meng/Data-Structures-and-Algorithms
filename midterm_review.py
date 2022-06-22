def revPrint(lst, low, high):
    if (low == high):
        print(lst[low])
    else:
        revPrint(lst, low+1, high)
        print(lst[low])


def function2(lst):
    if(len(lst) == 1):
        lst[0] = 0
        return 2
    return function2(lst[: len(lst)//2])


def function3(lst, low, high):
    if (low >= high):
        return 3
    for elem in lst:
        elem += 2
    return function3(lst, low+1, high-1)


def is_sorted(lst, low, high):
    result = True
    for i in range(low, high):
        if lst[i] > lst[i+1]:
            result = result and False
    return result

def remove_all_evens(lst):
    last_even = 0
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            lst[i], lst[last_even] = lst[last_even], lst[i]
            last_even += 1
    for i in range(last_even, len(lst)):
        lst.pop()
    return lst

def func(n):
    for i in range(1, n+1):
        yield 1/i

def seperate_num_v1(lst):
    ind_even = 0
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            lst[i], lst[ind_even] = lst[ind_even], lst[i]
            ind_even += 1
    return lst


def seperate_num_helper(lst, low, high):
    if low > high:
        return lst
    else:
        if lst[low] % 2 == 0:
            if lst[high] % 2 ==1:
                # temp = lst[low]
                # lst[low] = lst[high]
                # lst[high] = temp
                lst[low], lst[high] = lst[high], lst[low]
                return seperate_num_helper(lst, low+1, high-1)
            else:
                return seperate_num_helper(lst, low, high-1)
        else:
            return seperate_num_helper(lst, low+1, high)



def seperate_num_v2(lst):
    return seperate_num_helper(lst, 0, len(lst)-1)




lstA = [0, 0, 0, 0, 0, 0]
lstB = [3 ,1, 6, 2]
lst = [3, 15, 44, 2, 51, 89, 20]
n = 4

lst2= [1, 2, 3]
def func(lst):
    lst.append(4)
    lst = [5, 6, 7, 8]
    print("Inside", lst)


def count_up(start, end):
    if(start == end):
        print(start)
    else:
        count_up(start, end-1)
        print(end)




def count_down(start, end):
    if (start == end):
        print(start)
    else:
        print(end)
        count_down(start, end - 1)


print(count_down(0,5))

def count_up_v2(start, end):
    if (start == end):
        print(start)
    else:
        print(start)
        count_up_v2(start+1, end)


def factorial(n):
    if(n==1):
        return 1
    else:
        return factorial(n-1) * n
# print(factorial(5))




def func111(n):
    if (n<=1):
        return 0
    else:
        return 10 + func111(n-2)
# print(func111(16))


def func222(n):
    if (n<=1):
        return 1
    else:
        return 1 + func222(n//2)
# print(func222(16))


def func333(lst):
    if(len(lst) == 1):
        return lst[0]
    else:
        return lst[0] + func333(lst[1:])
lst333 = [1, 2, 3, 4, 5, 6, 7, 8]
# print(func333(lst333))

def sum_to(n):
    if n ==0:
        return 0
    else:
        return sum_to(n-1) + n

def product_evens(n):
    if n== 2:
        return 2
    else:
        return product_evens(n-2) * n

def product_evens_v2(n):
    if n==2:
        return 2
    else:
        if n% 2 == 0:
            return product_evens_v2(n-1) * n
        else:
            return product_evens_v2(n - 1)

# print(product_evens_v2(8))


def find_max(lst, low, high):
    if (low==high):
        return lst[low]
    else:
        if lst[low] < lst[high]:
            return find_max(lst, low+1, high)
        else:
            return find_max(lst, low, high-1)
lst_max = [13, 9, 16, 300, 4, 2]
# print(find_max(lst_max, 0, 5))

def pos_ints_list(n):
    if (n==1):
        return [1]
    else:
        rest = pos_ints_list(n-1)
        rest.append(n)
        return rest

# print(pos_ints_list(5))
# n= 3
# result = sum([i** 2 for i in range(1, n+1) if i % 2 != 0])
# print(result)

# result = [1* (10** i) for i in range(6)]
# print(result)

# result = [i * (i-1) for i in range(1, 11)]

# result = [for i in range]
# print(result)

def fibs(n):
    x = 1
    yield x
    y = 1
    yield y
    for i in range(n-2):
        z = x + y
        yield z
        x = y
        y = z

for curr in fibs(8):
    print(curr)




