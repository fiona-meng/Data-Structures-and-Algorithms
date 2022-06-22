import copy
# lst = [1, 2, [3, 4]]
# lst_copy = copy.copy(lst)
# lst[0] = 10
# lst_copy[2][0] = 30
# print(lst)
# print(lst_copy)

# lst = [1, [2, 3], ["a", "b"]]
# lst_slice = lst[:]
# lst_assign = lst
# lst.append("c")
# for i in range(1,3):
#     lst_slice[i][0] *= 2
# print(lst_slice)
# print(lst_assign)
# print(lst)

def sum_to(n):
    for i in range(1, n + 1):
        total = i * (i + 1) // 2
        yield total


# for i in sum_to(8):
#     print(i, end=", ")

# print([(-2)**i for i in range(8)])

# my_str = input("Enter a string: ")
# length = len(my_str)
# print([my_str[i] for i in range(-length, length)])


def muti_ones():
    for i in range(1,8):
        result = int("1" * i)
        yield result


# for i in muti_ones():
#     print(i)


def powers_of_two(n):
    x = 1
    yield x
    for i in range(1, n):
        x = x * 2
        yield x
#     everytime it stores x, right?

for i in powers_of_two(6):
    print(i)


class Polynomial:
    def __init__(self, lst):
        self.data = lst

    def __add__(self, other):
        lst = self.data.copy()
        temp = other.data.cop()
        if len(lst) > len(temp):
            # have lst be the shorter one
            lst, temp = temp, lst
        # extend lst with 0
        while len(lst) < len(temp):
            lst.append(0)
        lst = [lst[i] + temp[i] for i in range(len(lst))]
        return Polynomial(lst)

    def __call__(self, val):
        return sum([(val**i)*self.data[i] for i in range(len(self.data))])

    def __repr__(self):
        return "+".join([str(self.data[i] + "x^" + str(i) for i in range(len(self.data)-1, -1, -1))])

    def __mul__(self, other):
        pass
poly1 = Polynomial([32, 7, 0, -9, 2])
poly2 = Polynomial([2, 0, 0, 5, 0, 0, 3])
print(poly1(1))
print(poly2(1))
print(poly1)

