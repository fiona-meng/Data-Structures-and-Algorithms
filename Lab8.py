from ArrayStack import ArrayStack
from ArrayList import ArrayList


def stack_sum(s):
    if len(s) == 0:
        return 0
    else:
        val = s.pop()
        curr_total = stack_sum(s)
        curr_total += val
        s.push(val)
        return curr_total



s1 = ArrayStack()
s1.push(1)
s1.push(-14)
s1.push(5)
# print(stack_sum(s1))


def eval_prefix(exp_str):
    operators = "+-*/"
    exp_lst = exp_str.split()
    args_stack = ArrayStack()
    # Iterating from the back to the front
    for i in range(len(exp_lst)-1, -1, -1):
        token = exp_lst[i]
        # if token is an argument ( a number)
        if token not in operators:
            args_stack.push(int(token))
        else:
            arg1 = args_stack.pop()
            arg2 = args_stack.pop()
            if(token == '+'):
                res = arg1 + arg2
            elif (token == '-'):
                res = arg1 - arg2
            elif(token == '*'):
                res = arg1 * arg2
            elif(token == '/'):
                if(arg2 == 0):
                    raise ZeroDivisionError
                else:
                    res = arg1 / arg2
            args_stack.push(res)

    return args_stack.pop()

exp_str = "- + * 16 5 * 8 4 20"
# print(eval_prefix(exp_str))


def flatten_list(lst):
    stack = ArrayStack()

    while len(lst) != 0:
        val = lst.pop() # get the last value
        if isinstance(val, list): # is it a list?
            lst.extend(val) # extend it back
        else: # it is an int, its already flattened
            stack.push(val)
    while not stack.is_empty():
        lst.append(stack.pop())
        # remove the values from the stack and place back ino je list


# Q4
def stack_sort(s):
    helper = ArrayStack()

    while not s.is_empty():
        temp = s.pop()

        while(not helper.is_empty()) and temp < helper.top():
            s.push(helper.pop())

        if helper.is_empty() or temp> helper.top():
            helper.push(temp)
    while not helper.is_empty():
        s.push(helper.pop())




s2 = ArrayStack()
s2.push(3)
s2.push(1)
s2.push(5)
stack_sort(s2)
print(s2.pop())

