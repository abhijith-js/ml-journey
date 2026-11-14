# reverse_words(text)

# def reverse_words(text):
#     words=text.split()

#     return " ".join(reversed(words))


# print(reverse_words("Hello words"))



# is prime test

# def is_prime(num):
#     if num <2:
#         return False

#     for line in range(2,num):
#         if num%line==0:
#             return False

#     return True

# print(is_prime(10))

def is_prime(num):
    if num<2:
        return False

    for i in range(2,num):
        if num%i==0:
            return False

    return True

print(is_prime(10))
print(is_prime(5))
print(is_prime(-5))