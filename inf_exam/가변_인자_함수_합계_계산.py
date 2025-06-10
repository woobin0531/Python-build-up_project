def sum_many(*a):
    sum = 0
    for i in a:
        sum += i
    return sum

b = sum_many(1, 2, 4)
print(b)
