from itertools import permutations

def solution(l):
    l=sorted(l, reverse=True)
    #num permutations=P(n,k) = n!/(n-k)!
    perm = [permutations(map(str, l), r=i) for i in range(len(l), 0, -1)]
    for term in perm:
        for p in term:
            new_term=int("".join(p))
            if new_term % 3 == 0:
                return new_term
    return 0

# Test case 1
# print(solution([3, 1, 4, 1]))  # Output: 4311

# # Test case 2
# print(solution([3, 1, 4, 1, 5, 9]))  # Output: 94311