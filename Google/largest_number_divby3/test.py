from itertools import permutations

def solution(L):
    # Calculate the sum of all digits in the list
    total = sum(L)
    # Check if the total sum is divisible by 3
    if total % 3 == 0:
        # If the total sum is already divisible by 3, then return the digits in decreasing order
        return int(''.join(map(str, sorted(L, reverse=True))))
    else:
        # Otherwise, try to find the largest number that can be made by removing one or two digits
        # and checking if the remaining digits form a number divisible by 3
        for i in range(2, len(L)+1):
            for subset in permutations(L, i):
                if sum(subset) % 3 == 0:
                    return int(''.join(map(str, sorted(subset, reverse=True))))
    return 0
# Test case 1
print(solution([3, 1, 4, 1]))  # Output: 4311

# Test case 2
print(solution([3, 1, 4, 1, 5, 9]))  # Output: 94311