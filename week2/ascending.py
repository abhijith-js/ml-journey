def is_sorted(nums):
    if nums == sorted(nums):
        return True
    else:
        return False



print(is_sorted([1,4,5]))
print(is_sorted([]))
print(is_sorted([5]))
print(is_sorted([1, 2, 2, 3]))
print(is_sorted([3, 3, 3]))