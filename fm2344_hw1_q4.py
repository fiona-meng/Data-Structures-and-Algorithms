# list = [1, 10, 100, 1000, 10000, 100000]
[1 * (10 **i) for i in range(6)]

# list = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
print([i * (i - 1) for i in range(1, 11)])

# list = ["a", "b", "c", ..., "z"]
print([chr(i + 97) for i in range(26)])
