#!/usr/bin/env python3
import pprint


print("*********************************")
print("zip")

lst = [1, 2, 3], [4, 5, 6], [7, 8, 9]
lstz = list(zip(*lst))

pprint.pprint(lst, indent=4, width=20)
pprint.pprint(lstz, indent=4, width=20)

print("*********************************")
print("List comprehensions and iterators")
# iterator returns self
it = iter(range(20))
print(it, iter(it))
for i in it:
    print(i, next(it))
