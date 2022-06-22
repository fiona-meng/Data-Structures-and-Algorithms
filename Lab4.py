import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self, iter_collection = None):
        self.data_arr = make_array(1)
        self.capacity = 1
        self.n = 0

        if iter_collection is not None:
            for elem in iter_collection:
                self.append(elem)


    def __len__(self):
        return self.n


    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1


    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data_arr[i]
        self.data_arr = new_array
        self.capacity = new_size


    def __getitem__(self, ind):
        # if (not (0 <= ind <= self.n - 1)):
        #     raise IndexError('invalid index')
        # return self.data_arr[ind]
        if ind < 0:
            return self.data_arr[ind+3]
        elif 0 <= ind <= self.n - 1:
            return self.data_arr[ind]
        else:
            raise IndexError('invalid index')



    def __setitem__(self, ind, val):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if ind < 0:
            ind = self.n + ind
        self.data_arr[ind] = val


    def __iter__(self):
        for i in range(len(self)):
            yield self.data_arr[i]  #could also yield self[i]


    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)


    def __repr__(self):
        return (
                "[" + ", ".join("'" + val + "'"
                                if isinstance(val, str) else str(val) for val in self) + "]")


    def __add__(self, other):
        lst = ArrayList()
        lst += self
        lst += other
        return lst


    def __iadd__(self, other):
        self.extend(other)
        return self


    def __mul__(self, n):
        lst = ArrayList()
        for i in range(n):
            lst.extend(self)
        return lst


    def __rmul__(self, n):
        return self * n

    def remove(self, val):
        i = 0
        while i < self.n and self[i] != val:
            i += 1
        while i < self.n - 1:
            self[i] = self[i + 1]
            i += 1
        if i < self.n:
            self[i] = None
            self.n -= 1
        return self

    def removeAll(self, val):
        last_val = 0
        for i in range(len(self)):
            if self[i] != val:
                self[i], self[last_val] = self[last_val], self[i]
                last_val += 1

        while self[i] == val:
            self[i] = None
            i -= 1
            self.n -= 1
        return self


def find_pivot(lst):
    left = 0
    right = len(lst) - 1
    mid = left
    while left < right:
        mid = (left + right)//2
        if (lst[mid] > lst[right]):
            left = mid + 1
        else:
            right = mid
    return left


def shift_binary_search(lst, target):
    mid = find_pivot(lst)
    left = 0
    right = len(lst) - 1
    if lst[mid] <= target <= lst[right]:
        left = mid
    else:
        right = mid

