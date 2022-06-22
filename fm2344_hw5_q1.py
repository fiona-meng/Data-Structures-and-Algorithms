from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue
result_dic = {}
while True:
    operator = "+-*/"
    numbers = '1234567890'
    user_input = input("-->")

    if user_input == "done()":
        break
    elif len(user_input) == 1:
        print(result_dic[user_input])
    else:
        input_list = user_input.split()
        input_stack = ArrayStack()
        input_queue = ArrayQueue()
        for token in input_list:
            if token in numbers:
                input_stack.push(int(token))
            elif token in result_dic.keys():
                input_stack.push(int(result_dic[token]))
            elif token in operator:
                arg2 = input_stack.pop()
                arg1 = input_stack.pop()
                if token == "+":
                    res = arg1 + arg2
                    input_stack.push(res)
                elif token == "-":
                    res = arg1 - arg2
                    input_stack.push(res)
                elif token == "*":
                    res = arg1 * arg2
                    input_stack.push(res)
                elif token == "/":
                    if arg2 == 0:
                        raise ZeroDivisionError
                    else:
                        res = arg1 / arg2
                        input_stack.push(res)
            else:
                input_queue.enqueue(token)
        if not input_queue.is_empty():
            q1 = input_queue.dequeue()
            q2 = input_queue.dequeue()
            print(q1)
            result_dic[q1] = input_stack.pop()
        else:
            print(input_stack.pop())











