def most_frequent(lst):
    my_dic = {}
    for i in lst:
        if i not in my_dic:
            my_dic[i] = 1
        else:
            my_dic[i] += 1
    for i in my_dic:
