def shift(lst, k, direction="left"):
    if direction == "left":
        for i in range(k):
            letter = lst[0]
            for j in range(len(lst)-1):
                lst[j] = lst[j+1]
            lst[len(lst)-1] = letter
    else:
        for i in range(k):
            x = lst[-1]
            counter = len(lst) -1
            while counter > 0:
                lst[counter] = lst[counter-1]
                counter -= 1
            lst[0] = x
    return lst


def main():
    list = [1, 2, 3, 4, 5, 6]
    shift(list, 2, "right")
    shift(list, 2)






