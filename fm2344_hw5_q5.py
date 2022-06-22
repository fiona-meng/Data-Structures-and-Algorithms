from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack


def permutations(lst):
    my_stack = ArrayStack()
    my_queue = ArrayQueue()
    for i in lst:
        my_stack.push(i)
    for i in range(len(my_stack)) :
        element_stack = my_stack.pop()
        if my_queue.is_empty():
            my_queue.enqueue([element_stack])
        else:
            for j in range(len(my_queue)):
                element_queue = my_queue.dequeue()
                for i in range(len(element_queue) + 1):
                    current = element_queue.copy()
                    current.insert(i, element_stack)
                    my_queue.enqueue(current)
    result = []
    for i in range(len(my_queue)):
        result.append(my_queue.dequeue())
    return result



# lst = [1, 2, 3]
# print(permutations(lst))
