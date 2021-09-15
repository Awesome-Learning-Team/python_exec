def count_lower(input_string):
    counter = 0
    for i in str(input_string):
        if i.islower():
            counter += 1
    print(f"No. of Lower case characters: {counter}")


def count_upper(input_string):
    counter = 0
    for i in str(input_string):
        if i.isupper():
            counter += 1
    print(f"No. of Upper case characters: {counter}")


input_string = "The quick Brow Fox"

count_lower(input_string)
count_upper(input_string)
