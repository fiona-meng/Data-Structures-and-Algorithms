# developing a recursive algorithm
# step1: the base case
# solve the problem for the smallest possible input
# -identify how to measure the size of the input
# -find the condition testing for the smallest input
# -formulate the solution of the problem for the smallest possible input
# when calling count up with a smaller range, it would print the numbers in
# that range in an increasing order
def count_up_v1(start, end):
    if (start == end):
        print(start)
    else:
        count_up_v1(start, end-1)
        print(end)

def count_up_v2(start, end):
    if (start == end):
        print(start)
    else:
        print(start)
        count_up_v2(start+1, end)

def count_up_v3(start, end):
    if (start == end):
        print(start)
    else:
        mid = (start + end) // 2
        count_up_v3(start, mid)
        count_up_v3(mid+1, end)


# count_up(1,1) -> 1
# count_up(1,2) -> 1, 2
# count_up(1,3) -> 1, 2, 3
# count_up(1,4) -> 1, 2, 3, 4
count_up_v3(1, 8)