def knapsack(weight_cap, weights, values):
    n = len(values)
    K = [[0 for x in range(weight_cap + 1)] for x in range(n + 1)]
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(weight_cap + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i-1] <= w:
                K[i][w] = max(values[i-1] + K[i-1][w-weights[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
  
    return K[n][weight_cap]
        

weight_cap = 10
weights = [3, 6, 8, 100, 50]
valuesues = [50, 60, 100, 200, 50]
print(knapsack(weight_cap, weights, valuesues))


