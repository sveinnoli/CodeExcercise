from random import randint
l1=[1,1,3,4,5,9] # sorted=[9,5,4,3,1,1] solution = 9+5+4+3 = 21
l1= [randint(1,9) for n in range(100)]# sorted=[9,5,4,3,1,1] solution = 9+5+4+3 = 21
from math import log

def solution(l):
    largest_sum=sum(l)
    l=sorted(l, reverse=True)
    if largest_sum%3==0: return "".join(map(str, l))

    # total number of elements in subset is 2^len(l)
    subset=[0]
    for num in l:
        new_subset = [s + num for s in subset]
        subset+=new_subset

    # Find indices of numbers that sum up to largest sum that is %3==0
    largest=(-1,-1)
    for i, s in enumerate(subset):
        if s > largest[1] and s % 3 == 0:
            largest=(i, s)

    # in the case 0 was the only valid sum.
    if largest[0] == 0: return 0
    
    exp=log(largest[0], 2)
    # in the case a single character was the solution.
    if exp == int(exp):
        return largest[1]
    else:
        # in the case more than 1 character was the solution.
        characters=[]
        while exp > 0:
            new_exp=log(largest[0]-1, 2)
            new_index = largest[0]-2**int(new_exp)
            current_char = 2**int(exp)
            characters.append(subset[current_char])
            exp -=1
            
            if log((new_index), 2) == int(log(new_index, 2)):
                break
        return "".join(map(str, sorted(characters, reverse=True)))
print(solution(l1))

