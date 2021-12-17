def score_sorter(array):
    top_score = 0

    for outer_index, val in enumerate(array):
        top_score = 0
        for inner_index in range(outer_index, len(array)):
            score = array[inner_index]
            if score > top_score:
                #Swap val with top score
                lw = array[outer_index]
                array[outer_index],array[inner_index] = score, lw
                top_score = score
    return array

print(score_sorter([1,2,3,9999,13, 12, 1, 21 ,12,1 ,22]))