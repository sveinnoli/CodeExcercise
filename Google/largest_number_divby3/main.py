from itertools import permutations

from largest_number_divby3 import solution as s1
from largest_number_divby3_v2 import solution as s2

l=list([permutations(range(1, 10), r=i) for i in range(9, 0, -1)])
for perm in l:
    for n in perm:
        res1= s1(n)
        res2= s2(n)
        if res1 != res2:
            print(f"input: {n} gave invalid output: r1: {res1}, r2: {res2}")

