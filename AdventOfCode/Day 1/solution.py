with open("input.txt", "r") as f:
    _sum = 0
    sums = []
    lines = f.read().splitlines()
            
    for line in lines:
        if line:
            _sum += int(line)
        else:
            sums.append(_sum)
            _sum = 0

    # # Alternate way of finding n biggest sums
    # sums = sorted(sums)
    # print(sum(sums[:-4:-1]))
    
    for n in range(0, len(sums)):
        for j in range(0, len(sums) - n - 1):
            if sums[j] > sums[j + 1]:
                sums[j] += sums[j + 1]
                sums[j + 1] = sums[j] - sums[j + 1]
                sums[j] -= sums[j + 1]
    print(sum(sums[:-4:-1]))
