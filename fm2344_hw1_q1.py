lst1 = [1, 2, 3]
lst2 = [lst1 for i in range(3)]
print(lst2)
lst2[0][0] = 10
print(lst2)