def fibonacci(num):
    if num < 0:
        raise ValueError("Negative number not allowed!")
    elif num == 0:
        return []
    elif num == 1:
        return [0]
    
    my_list = []
    my_list.append(0)
    my_list.append(1)

    while len(my_list) < num:
        next_num = my_list[-2] + my_list[-1]
        my_list.append(next_num)

    return my_list


print(fibonacci(-1))