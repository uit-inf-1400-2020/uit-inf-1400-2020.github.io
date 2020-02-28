#!/usr/bin/env python3

# reversed

normal_list = [1, 2, 3, 4, 5]


class CustomSequence():
    def __len__(self):
        return 5

    def __getitem__(self, index):
        return "x{0}".format(index)


class FunkyBackwards(CustomSequence):
    def __reversed__(self):
        return "BACKWARDS!"


for seq in normal_list, CustomSequence(), FunkyBackwards():
    print("{}: ".format(seq.__class__.__name__), end="")
    for item in reversed(seq):
        print(item, end=", ")
    print()


comb = [(x, y) for x in [1, 2, 3]
               for y in [3, 1, 4]
        if x != y]
print('Comb is', comb)


def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1


def fibonacci():
    "Generates an infinite sequence of Fibnacci numbers"
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# get the first few Fibonacci numbers
for i, v in enumerate(fibonacci()):
    print("Fib #{} is {}".format(i, v))
    if i > 10:
        break
