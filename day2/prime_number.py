import math


def is_prime_number(num):
    if num < 2:
        return False
    if num >= 2 and num <= 3:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


for i in range(1, 100):
    if is_prime_number(i):
        print(i)
