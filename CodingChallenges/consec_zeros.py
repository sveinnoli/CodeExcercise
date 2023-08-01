from random import randint
from time import time

def consecutive_zerosv1(binary: str) -> int:
    max_0 = 0
    curr_0 = 0
    for n in list(binary):
        if n == "0":
            curr_0 += 1
        else:
            max_0 = max(max_0, curr_0)
            curr_0 = 0
    return max_0

def consecutive_zerosv2(binary: str) -> int:
    return max([len(s) for s in binary.split("1")])

# Generate bin str
a = "".join(["1" if randint(1,2) == 2 else "0" for n in range(1000000)])

# Method 1
s = time()
r = consecutive_zerosv1(a)
print(f"Method 1: Time: {time()-s}, result={r}")


# Method 2
s = time()
r = consecutive_zerosv2(a)
print(f"Method 2: Time: {time()-s}, result={r}")
