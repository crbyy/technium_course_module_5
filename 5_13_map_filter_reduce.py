from functools import reduce

#1
def cubes(x):
    return x ** 3

numbers = [1, 2, 3, 4, 5]
cubed = list(map(cubes, numbers))

print(cubed)


#2
def is_div(x):
    return x % 5 == 0

numbers = [42, 45, 90, 3, 55, 91, 25, 78, 5, 33]
filtered = list(filter(is_div, numbers))

print(filtered)

#3

def is_odd(x):
    return x % 2 != 0

def multiply(x, y):
    return x * y

numbers = [14, 7, 20, 4, 11, 19, 5, 8, 15, 2]
filtered = list(filter(is_odd, numbers))

multiplied = reduce(multiply, filtered)

print(filtered)
print(multiplied)

