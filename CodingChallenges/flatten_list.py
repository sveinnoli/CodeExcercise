import time
from itertools import chain
from functools import reduce

def flatten_array(arr):
    for o_index, n in enumerate(arr):
        if isinstance(n, list):
            for i_index, i in enumerate(arr[o_index]):
                arr.insert(o_index+i_index+1, i)
            del arr[o_index]  
    return arr 
    
def reduce_add(lsts):
    return reduce(lambda x, y: x + y, lsts)

def nested_list_comprehension(lsts):
    return [item for sublist in lsts for item in sublist]

def flatten(items):
    """Yield items from any nested iterable; see REF."""
    for x in items:
        if isinstance(x, Iterable):
            yield from flatten(x)
        else:
            yield x

listi = [n for n in range(10000) for n in range(10000)]

# start = time.perf_counter()
# (flatten_array(listi))
# end = time.perf_counter()
# print(end-start)


start = time.perf_counter()
flatten(listi)
end=time.perf_counter()
print(end-start)


