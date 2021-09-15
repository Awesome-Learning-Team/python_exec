def max(a, b):
    if a > b:
        return a
    return b


def max_three_number(a, b, c):
    return max(max(a, b), c)


print(max_three_number(1, 2, 3))
