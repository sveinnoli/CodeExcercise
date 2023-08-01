from two_sum import Solution

from time import time
from random import randint
array = [randint(1, 10000) for n in range(100000)]
start=time()
s = Solution()
a=s.twoSum(array, randint(5000, 10000))
end = time()
print(f"Time: {end-start}s, solution: {a}")