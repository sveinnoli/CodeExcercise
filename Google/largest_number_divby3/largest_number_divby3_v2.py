def solution(l):
    # Compute the sum of all the digits in the input list
    digit_sum = sum(l)

    # Sort the list in non-increasing order
    l = sorted(l, reverse=True)

    # Try to remove the fewest number of digits to obtain a number
    # that is divisible by 3
    for i in range(len(l)):
        if digit_sum % 3 == 0:
            # The sum of the remaining digits is divisible by 3
            break
        elif (digit_sum - l[i]) % 3 == 0:
            # Removing the i-th digit makes the sum divisible by 3
            digit_sum -= l[i]
            l.pop(i)
            break

    # If the remaining digits do not form a number that is divisible by 3,
    # return 0 as the solution
    if digit_sum % 3 != 0:
        return 0

    # Construct the largest number that is divisible by 3 using the
    # remaining digits
    return int(''.join(map(str, sorted(l, reverse=True))))


# print(solution([3, 1, 4, 1]))  # Output: 4311

# # Test case 2
# print(solution([3, 1, 4, 1, 5, 9]))  # Output: 94311