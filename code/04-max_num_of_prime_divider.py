import math

def is_prime(num):
    if num == 1 or num == 4 or num == 6 or num == 8 or num == 9:
        return 0
    if num == 2 or num == 3 or num == 5 or num == 7 or num == 11:
        return 1

    counter = 0
    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % i == 0:
            counter = counter + 1
    
    if counter > 0:
        return 0
    else:
        return 1

def num_of_prime_dividers(num):
    counter = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0 and is_prime(i):
            counter = counter + 1
    return counter

nums_prime_dividers = []
for i in range(10):
    tmp = int(input())
    nums_prime_dividers.append((tmp, num_of_prime_dividers(tmp)))

nums_prime_dividers.sort(key = lambda x: (-x[1], -x[0]))

# print(nums_prime_dividers)
print(nums_prime_dividers[0][0], nums_prime_dividers[0][1])

# x = [12, 21, 37, 4 ,5,61,7,8,9, 10, 2]
# print(x[0], is_prime(x[0]))
# print(x[1], is_prime(x[1]))
# print(x[2],is_prime(x[2]))
# print(x[3],is_prime(x[3]))
# print(x[4],is_prime(x[4]))
# print(x[5],is_prime(x[5]))
# print(x[6],is_prime(x[6]))
# print(x[7],is_prime(x[7]))
# print(x[8],is_prime(x[8]))
# print(x[9],is_prime(x[9]))
# print(x[10],is_prime(x[10]))

# print(x[0], num_of_prime_dividers(x[0]))
# print(x[1], num_of_prime_dividers(x[1]))
# print(x[2],num_of_prime_dividers(x[2]))
# print(x[3],num_of_prime_dividers(x[3]))
# print(x[4],num_of_prime_dividers(x[4]))
# print(x[5],num_of_prime_dividers(x[5]))
# print(x[6],num_of_prime_dividers(x[6]))
# print(x[7],num_of_prime_dividers(x[7]))
# print(x[8],num_of_prime_dividers(x[8]))
# print(x[9],num_of_prime_dividers(x[9]))
# print(x[10],num_of_prime_dividers(x[10]))

# ------------- input ------------
# 123
# 43
# 54
# 12
# 76
# 84
# 98
# 678
# 543
# 231

# ----------- output -------------
# 678 3