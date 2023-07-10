from random import randint
BAG_SIZE    = 10**5
WEIGHT_SIZE = randint(BAG_SIZE, 10**5)
weights=[randint(1, 10) for _ in range(WEIGHT_SIZE)]

class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        n = len(weights)
        cumulative_sum = [0] * (n + 1)

        # Calculate the cumulative sum of weights
        for i in range(1, n + 1):
            cumulative_sum[i] = cumulative_sum[i-1] + weights[i-1]

        max_difference = 0

        # Iterate over the indices of weights from 0 to (n - k)
        for i in range(n - k + 1):
            difference = cumulative_sum[i+k] - cumulative_sum[i]
            max_difference = max(max_difference, difference)

        return max_difference


s=Solution()
result = s.putMarbles([1,3,5,1], 2)
print(result)