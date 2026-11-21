def find_avg(data):
    if not data:
        raise ValueError("Can't process calculation check your input numbers")
    
    total = 0
    for num in data:
        total += num

    return total / len(data)



try:
    print(find_avg([10,20,30]))
except ValueError as e:
    print("Error:", e)