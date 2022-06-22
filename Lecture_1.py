### 1 ###
lst = [1, 2, 3]
for elem in lst:
    elem += 10
    # print(elem)

lst = [1, 2, 3]
for ind in range(len(lst)):
    lst[ind] += 10
# print(lst)



### 2 ###
# append method is mutable, so it refers to old data
lst1 = [1, 2, 3]
lst2 = lst1
lst3 = [1, 2, 3]
lst1.append(4)
# lst1 = [1, 2, 3, 4, 5]
lst2.append(5)
# lst2 = [1, 2, 3, 4, 5]
lst3.append(6)
# lst3 = [1, 2, 3, 6]
# print("lst1 =", lst1)
# print("lst2 =", lst2)
# print("lst3 =", lst3)

### 2.5 ###
# 7
#
# String is immutable because there is no way to change the
# contents of its internal representation, no way to gain a
# reference to its internal representation, and it cannot be
# subclassed. This means that no matter what you do to a String,
# you cannot change its contents.
s1 = "abc"
s1.upper()
# print(id(s1)) 140224054694896
# print(id(s1.upper())) 140224074754992
# string is immutable, so the upper method create a new object with old content
print("s1 =", s1)
s2 = s1.upper()
print("s1 =", s1)
print("s2 =", s2)



### 3 ###
def main():
    lst = [1, 2, 3]
    s = "abc"
    func(lst, s)
    print("main: lst =", lst, "s =", s)


def func(lst, s):
    for ind in range(len(lst)):
        lst[ind] += 10
    lst.append(5)
    # s.upper()
    s = s.upper()
    print("fun: lst =", lst, "s =", s)

# list is mutable, but string is immutable
main()



### 4 ###
import copy
lst1 = [1, 2, 3, 4]
lst2 = copy.copy(lst1)
lst2[0] = 10
# print(lst1)  [1, 2, 3, 4]
# print(lst2) [10, 2, 3, 4]
# see lst1 didn't change
lst1 = [1, [2, 3], 4]
lst2 = copy.copy(lst1)
lst2[0] = 10
lst2[1][0] = 20
# print(lst1) [1, [20, 3], 4]
# print(lst2) [10, [20, 3], 4]
# Shallow Copy stores the references of objects to the original memory address
# Deep copy stores copies of the object’s value

# Shallow Copy reflects changes made to the new/copied object in the
# original object. (faster)
# Deep copy doesn’t reflect changes made to the new/copied object in
# the original object. (comparatively slower)


lst1 = [1, [2, 3], 4]
lst2 = copy.deepcopy(lst1)
lst2[0] = 10
lst2[1][0] = 20
# print(lst1) [1, [2, 3], 4]
# print(lst2) [10, [20, 3], 4]


### 5 ###
class Counter:
    def __init__(self):
          self.value = 0
    def inc(self):
          self.value += 1
    def __repr__(self):
        return str(self.value)


c1 = Counter()
c1.inc()
c1.inc()
c1.inc()
c1
# 3

c2 = Counter()
c2.inc()
c2
# 1


lst1 = [Counter() for i in range(3)]
# [0, 0, 0]
# list comprehension: immutable
for c in lst1:
    c.inc()
    print(c)

lst2 = [Counter()]*3
# mutable
# [0, 0, 0]
for c in lst2:
    c.inc()
    print(c)



### 6 ###
lst1 = [1, 2, 3]
lst2 = [4, 5]
print("before extend, lst1:", id(lst1))

lst1.extend(lst2)
print("after extend, lst1:", id(lst1))
# same

lst1 = [1, 2, 3]
lst2 = [4, 5]
print("before +, lst1:", id(lst1))

lst1 = lst1 + lst2
print("after +, lst1:", id(lst1))


lst1 = [1, 2, 3]
lst2 = [4, 5]
print("before +=, lst1:", id(lst1))

lst1 += lst2
print("after +=, lst1:", id(lst1))
