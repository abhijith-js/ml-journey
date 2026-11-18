def fibonacci(num):
    if num==0:
        return []
    elif num==1:
        return [0]
    my_list=[]
    my_list.append(0)
    my_list.append(1)
    next_num=[]

    while len(my_list)<num:
        my_list[-2] + my_list[-1]
        next_num.append(my_list)


    return next_num


print(fibonacci(6))

    




