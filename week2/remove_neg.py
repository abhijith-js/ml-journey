def remove_neg(data):
    pos=[]
    for line in data:
        if line>=0:
            pos.append(line)


    return pos


print(remove_neg([3, -1, 0, -5, 7]))
print(remove_neg([]))
