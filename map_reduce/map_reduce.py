from functools import reduce


def sum(x, y):
    return x+y


def sub(x, y):
    return x-y


def mul(x, y):
    return x*y


def div(x, y):
    return x/y


list_a = [10, 20, 30, 40, 50]
list_b = [10, 20, 30, 40, 50]

list_b.sort(reverse=True)

# map functions

list_sum = list(map(sum, list_a, list_b))
print(list_sum)

list_sub = list(map(sub, list_a, list_b))
print(list_sub)

list_mul = list(map(mul, list_a, list_b))
print(list_mul)

list_div = list(map(div, list_a, list_b))
print(list_div)

list_pow_a = list(map(lambda x: x ** 2, list_a))
print(list_pow_a)

list_pow_b = list(map(lambda y: y ** 2, list_b))
print(list_pow_b)

# reduce functions

red_sum = reduce(sum, list_a)
print(red_sum)

red_sub = reduce(sub, list_a)
print(red_sub)

red_mul = reduce(mul, list_a)
print(red_mul)

red_div = reduce(div, list_a)
print(red_div)

red_max = reduce(lambda x, y: max(x, y), list_a)
print(red_max)

# filter functions

filter_over_10 = list(filter(lambda x: x > 10, list_a))
print(filter_over_10)

filter_over_20 = list(filter(lambda x: x > 20, list_a))
print(filter_over_20)

filter_over_30 = list(filter(lambda x: x > 30, list_a))
print(filter_over_30)

filter_over_40 = list(filter(lambda x: x > 40, list_a))
print(filter_over_40)

filter_over_50 = list(filter(lambda x: x > 50, list_a))
print(filter_over_50)

# list comprehensions (more agility for map)

list_a = [x for x in list_a]
print(list_a)

list_a_over_10 = [x for x in list_a if x > 10]
print(list_a_over_10)

list_a_over_20 = [x for x in list_a if x > 20]
print(list_a_over_20)

list_a_over_30 = [x for x in list_a if x > 30]
print(list_a_over_30)

list_a_over_40 = [x for x in list_a if x > 40]
print(list_a_over_40)

list_a_over_50 = [x for x in list_a if x > 50]
print(list_a_over_50)
