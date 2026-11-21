def count_pos(data):
    if not data: 
        return 0
    count=[]
    for num in data:
        if num > 0:
            count.append(num)

    return len(count)


print(count_pos([3, -1, 0, 7]))
