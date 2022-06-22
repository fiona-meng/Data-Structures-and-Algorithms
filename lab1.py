import random
# lst = [1, 2, 3]
# def func(lst):
#     lst.append(4)
#     lst = [5, 6, 7, 8]
#     print(lst)
# func(lst)
# print(lst)



word_1 = "apple"
letters_1 = "aples"
letters_2 = "aplespl"


def can_construct(word, letters):
    word_list = list(word)
    letters_list = list(letters)

    for x in letters_list:
        if x in word_list:
            word_list.remove(x)

    if word_list:
        print(False)
    else:
        print(True)


can_construct(word_1, letters_1)
can_construct(word_1, letters_2)


def can_construct2(word, letters):
    letters_lst = [-1] * 26
    for char in letters:
        if letters_lst[ord(char)-97] == -1:
            # letters_lst[ord(char-97)] = 0
            letters_lst[ord(char)-97] += 1
    for char in word:
        if letters_lst[ord(char)-97] == -1:
            return False
        if letters_lst[ord(char)-97] < 1:
            return True


class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Complex(self.a * other.b + (self.b * other.b)*(-1),
                       self.a * other.b + self.b * other.a)

    def __str__(self): # what is different between str and repr
        return str(self.a) + " + " + str(self.b) + "i"

    def __iadd__(self, other):
        self = self + other
        return self

cplx1 = Complex(5, 2)
cplx2 = Complex(3, 3)
cplx2 += cplx1
print(cplx1)
print(cplx2)


def create_permutation(n):
    new_list = [-1] * n
    counter = 0
    while counter < n:
        x = random.randint(0, n-1)
        if new_list[x] == -1:
            new_list[x] = counter
            counter += 1
    return new_list


def scramble_word(word):
    word_list = list(word)
    index = create_permutation(len(word))
    result = []
    for i in index:
        result.append(word_list[i])
    return "".join(result)


scramble_word("pokemon")


def guessing_game(word):
    puzzle = scramble_word(word)
    print("Unscramble the word:" + puzzle)
    try_times = 3
    correct_guess = False
    for i in range(try_times):
        guess = input("Try #" + str(4-try_times) + ":")
        if guess == word:
            correct_guess = True
            print("Yay, you got it")
            break
        else:
            print("Wrong")
            try_times -= 1
guessing_game("Hello")