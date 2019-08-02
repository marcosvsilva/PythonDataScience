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
