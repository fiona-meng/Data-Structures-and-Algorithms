def findChange(lst01):
    left = 0
    right = len(lst01) - 1
    ind = None
    found = False
    while (found == False) and (left<= right):
        if lst01[0] == 1:
            return 0
        mid = (left + right)//2
        if (lst01[mid] == 0):
            left = mid + 1
        elif (lst01[mid] == 1):
            if lst01[mid - 1] == 0:
                ind = mid
                found = True
            else:
                right = mid - 1
    return ind


def main():
    lst = []
    print(findChange(lst))


